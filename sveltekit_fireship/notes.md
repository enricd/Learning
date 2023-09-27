## Key Concepts - Fireship SvelteKit Course

### 1. Create a SvelteKit App

- Requirements:
  - [ ] Node.js 18+ 

- Steps:
  - $ npm create svelte@latest myapp
  - Select skeleton project, TS (or JS) and skip following stepsmy
  - $ cd myapp
  - $ npm i             # install dependencies
  - $ npm run dev       # run dev server
  - Create a src/lib/ directory if it's not already there, it can be imported anywhere with $lib


### 2. SvelteKit DevTools

- Svelte for VS Code plugin
  - Once installed, it allows to auto-generate boilerplate for different examples with right click for example in the src/routes folder. It can also be accessed from the vscode command palette with the command "SvelteKit: Create ..."
  - You can also select one fragment of the code to extract it as a component with selecting it and doing right click and selecting "Svelte: Extract Component" or with the command "SvelteKit: Extract to component"

- Thunder Client plugin: http client to test api endpoints

- Inline fold plugin: allows to fold code blocks with a comment like // #region or // #endregion

- Web vitals plugin for chrome


### 3. Routing

- SvelteKit uses the file system to define routes. The file system is the API. The file system is the router.
  
- Inside the routes/ directory every directory that we create will be a new url path. They can be also dynamic by using square brackets like [id]. The framework will detect it as a url parameter accessible from anywhere else.

- The page store allows to access to the url parameters from the client side {$page.params.username} and they are updated reactively.

- Svelte has 4 special filenames that are prefixed with a + sign: page, layout, server and error. They can end with .svelte, .ts, or .server.ts

- On the initial page load the server will render the page and send it to the client (better for SEO). After the initial page load, svelte will hydrate the page (the client side javascript will take over and will be able to render subsequent navigations client side which is typically faster and more efficient with better UX).

- If you are building a website that doesn't fetch data from any API or DB you can build it only using **+page.svelte** files that can build the UI and run on server and client. A **+page.ts** file can fetch data both on the server and on the client. **+page.server.ts** can fetch data but only runs on the server. 

- **+layout.** work similarly to +page.* but their UI can be shared accross multiple child routes.

- **+server.ts** routes are only run on the server and can be used to fetch data from an API or DB without returning any HTLM but JSON and other response types.

- **+error.svelte** is used to handle errors. It can be used to display a custom error page or to redirect to another page.


### 4. Data Fetching

- In SvelteKit there are 3 different ways of fetch data: Client-side (+page.svelte), Server-side (+page.server.ts) and a hybrid of both (+page.ts).

- **Client-side** data fetching:
  - Everything happens on the browser after the initial page load. This is the typical way you would do things in Svelte without the Kit. Create a +page.svelte file.
  - we import { onMount } from "svelte"; lifecycle hook
  - then we create state
  - then we fetch data and set state
  - this data won't be available to search engines or social media crawlers
  - in general client-side data fetching is ideal for private data, e.g. content for an authenticated user

- **Server-side** data fetching:
  - create a new +page.server.ts file in the same directory as the +page.svelte file the component that needs that data.
  - that file imports PageServerLoad from ./$types and exports a load function that will be executed when the user navigates that page.
  - it returns an object of data that will be accessable automatically to the Svelte component.
  - You can do anything on the backend, like fetch data from an API, db SDK, acces .env vars, use raw sql queries to a db or access the file system, as this code will only run on the server and won't be on the client-side.
  - If you go to the Svelte component (+page.svelte) you will see that we have access to that data that has a type of $page.data
  - Sveltekit generates this interface automatically so we get end-to-end type safety from the back to the front.

- **Hybrid** data fetching:
  - Sometimes we don't need a server to do data fetch. Create a +page.ts file.
  - This code can run both in client-side and server-side. Server-side on the initial load and client-side on subsequent navigations.
  - It won't be possible ot access to private .env vars, use the admin SDK or access the file system.

- Fetching data from the page **$app/stores**
  - We can also fetch data from the page $app/stores. This is useful for data that needs to be shared across multiple pages as the data that is fetched there is accessible from anywhere in the app.