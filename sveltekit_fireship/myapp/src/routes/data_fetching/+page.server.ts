// Server-side data fetching

import type { PageServerLoad } from './$types';

export const load = (async () => {

    // fetch some data from the server

    return {
        title: "My data",
        text: "Hi everyone!"
    };
}) satisfies PageServerLoad;