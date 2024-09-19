// Algolia code: refer: https://www.algolia.com/doc/guides/building-search-ui/installation/js/#directly-in-your-page

const searchClient = algoliasearch(
  "BLBFWG8F8W",
  "8ddbd72ba6b0d04c51c5ccc03e7e08b4"
);

const search = instantsearch({
  indexName: "blogs_BlogPost",
  searchClient,
});

search.addWidgets([
  instantsearch.widgets.searchBox({
    container: "#searchbox",
  }),
  instantsearch.widgets.refinementList({
    container: "#published-list",
    attribute: "published",
  }),
  instantsearch.widgets.clearRefinements({
    container: "#clear-refinements",
  }),

  instantsearch.widgets.hits({
    container: "#hits",
    templates: {
      item: `
        <a style="color: black;" href="${window.location.origin}/blogs/{{slug}}">
          <div> {{#helpers.highlight}}{ "attribute": "title" }{{/helpers.highlight}} </div>
        </a>
              `,
    },
  }),
]);

search.start();
