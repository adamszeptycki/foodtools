/// <reference path="./.sst/platform/config.d.ts" />


export default $config({
  async app(input) {
    const  { Stage }  = await import( "./infra/stages");
    return {
      name: "foodtools",
      protect: input?.stage === Stage.PROD,
      removal: input?.stage === Stage.PROD ? "retain" : "remove",
      home: "aws",
    };
  },
  async run() {
    await import("./infra/config");
    await import("./infra/storage");
    await import("./infra/queue");
    await import("./infra/router");
    const { nextJsPage } = await import("./infra/nextPage");
    return {
      nextJsPage: nextJsPage.url,
    };
  },
});
