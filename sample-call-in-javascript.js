import "dotenv/config";
import OpenAI from "openai";
import { getBearerTokenProvider, DefaultAzureCredential } from "@azure/identity";

const endpoint = process.env.AZURE_OPENAI_ENDPOINT;
const deploymentName = process.env.AZURE_OPENAI_DEPLOYMENT || "gpt-4.1-mini";
// const tokenProvider = getBearerTokenProvider(
//     new DefaultAzureCredential(),
//     'https://ai.azure.com/.default');

const openai = new OpenAI({
    baseURL: endpoint,
    apiKey: process.env.AZURE_OPENAI_API_KEY
});

async function main() {
  const runner = openai.responses
    .stream({
      model: deploymentName,
      input: 'what is \"Knowledge\"?',
    })
    .on('event', (event) => console.log(event))
    .on('response.output_text.delta', (diff) => process.stdout.write(diff.delta));

  for await (const event of runner) {
    console.log('event', event);
  }

  const result = await runner.finalResponse();
  console.log(result.output_text);
}

main();
