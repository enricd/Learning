// hybrid data fetching

import type { PageLoad } from './$types';

export const load = (async () => {

    const { title, text } = await fetch('someAPI').then(res => res.json());

    return {
        title,
        text
    };
}) satisfies PageLoad;