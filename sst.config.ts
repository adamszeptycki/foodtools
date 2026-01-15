/// <reference path="./.sst/platform/config.d.ts" />

// import { Stage } from "./infra/stages";

export default $config({
  async app(input) {
    const  { Stage }  = await import( "./infra/stages");
    return {
      name: "foodtools",
      removal: input?.stage === Stage.PROD ? "retain" : "remove",
      protect: input?.stage === Stage.PROD,
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
