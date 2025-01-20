import inspect
from fastapi import Form


def as_form(cls):
    """
    Decorator that adds an 'as_form' class method to a Pydantic model,
    allowing it to be instantiated from form data submitted via an HTTP request.
    """
    new_params = []
    # Iterate over all the fields defined in the Pydantic model
    for field_name, model_field in cls.model_fields.items():
        # For each field, create a new parameter for the function signature
        new_params.append(
            inspect.Parameter(
                field_name,
                inspect.Parameter.POSITIONAL_OR_KEYWORD,  # The parameter can be passed positionally or as a keyword
                # Set the default value using Form(...)
                default=Form(...) if model_field.is_required() else Form(model_field.default),
                # Set the annotation (type hint) to the field's type
                annotation=model_field.annotation,
            )
        )

    # Define a new asynchronous class method that will be used to instantiate the model from form data
    async def as_form_func(cls, **data):
        return cls(**data)

    # Retrieve the signature of the 'as_form_func' method
    sig = inspect.signature(as_form_func)
    # Replace the parameters of the signature with the new parameters created from the model fields
    sig = sig.replace(parameters=[inspect.Parameter('cls', inspect.Parameter.POSITIONAL_OR_KEYWORD)] + new_params)
    # Assign the updated signature to the 'as_form_func' method
    as_form_func.__signature__ = sig
    # Add the 'as_form' method to the class as a classmethod
    setattr(cls, 'as_form', classmethod(as_form_func))
    # Return the modified class
    return cls