# Experimenting with Similarity Search in a Vector DB

The following generations were conducted with and without using similarity search on the Vector DB. 
1. [Clinical Note Generation](#clinical-note-generation)
2. [Response Generation to Specific Questions](#response-generation-to-specific-questions)

## Clinical Note Generation

The Anthropic Claude v3 Sonnet model was asked to generate a clinical note based on a [sample clinical note](./sample_responses/clinical-notes-01.txt). 

### With embedding (titan.v2) and similarity selection

With embedding and selection of the 20 most relevant rows from the csv file, the model does not have a lot of data to work with (since those 20 most relevant rows are very similar). 

View one of the better textual responses here: [attempt-8](./results/clinical-notes-01/attempt-8.txt)

View one of the better JSON responses here: [attempt-10](./results/clinical-notes-01/attempt-10.txt) (the JSON is cut off due to the token limit set)

JSON response is largely a copy-and-paste of some of the data passed in. 

### Using titan.v1 Embedding

Does worse than when using titan.v2 embedding in its textual response, in which direct lifting of the textual data into the response is observed. JSON response, similar to when titan.v2 embedding is used, also involves direct copying. 

Textual response: [attempt-13](./results/clinical-notes-01/attempt-13.txt)

JSON response: [attempt-14](./results/clinical-notes-01/attempt-14.txt)

### Using the entire csv file

When generated in textual format, the model seems to be able to summarize the provided csv file to produce a concise clinical note. See [control-attempt-3](./results/clinical-notes-01/control-attempt-3.txt). 

However, in JSON, the model only regurgitates some of the phrases provided to it. See [control-attempt-4](./results/clinical-notes-01/control-attempt-4s.txt)

### Issues with both Methods

1. When the sample response is placed in front of the data provided, the model interprets the sample clinical note as data (i.e. information from the sample is included in the generated clinical note). This may be because the sample clinical note is in JSON. 

2. The model does not use JSON format even though that is specified in the prompt to follow that of the sample (which is in JSON)
    - It only uses JSON format even when specifically prompted to output in JSON. 

3. The JSON output does not summarize the provided input. It is largely a copy-and-paste of some chunks of the textual data provided. 

### Transferable Takeaways

The model places greater emphasis on the first tokens passed to it, even though the total context window size is 200k (see [Anthropic documentation on Claude hosted on AWS Bedrock](https://docs.anthropic.com/en/docs/about-claude/models)). 

### Recommendations

- Can consider having the sample clinical note / referral letter be in continuous text format, since that is what the model expects
- Pass the sample response after the data to minimize the model's incorporation of data from the sample response into the final output

## Response Generation to Specific Questions

The Anthropic Claude v3 Sonnet model was asked to generate a response to a question about the [data provided](./data/csv_xlsx/chan-RenalGenie_Clinical_Note_csv.csv). 

Specifically, the question was to report on the stability of the patient. 

### With embedding and selection

With embedding and selection of the 20 most relevant rows from the csv file, the response is relevant and is relatively well-formatted (for the JSON response). 

View the textual response here: [attempt-12](./results/clinical-notes-01/attempt-12.txt)

View the JSON response here: [attempt-11](./results/clinical-notes-01/attempt-11.txt)

### Using the entire csv file

Relatively mediocre result. Model does not register sample response, and does not take up the identity of a specialist in drafting clinical documents, instead answering in a manner that the normal sensible human would. 

View the textual response here: [control-attempt-6](./results/clinical-notes-01/control-attempt-6.txt)

View the JSON response here: [control-attempt-5](./results/clinical-notes-01/control-attempt-5.txt)