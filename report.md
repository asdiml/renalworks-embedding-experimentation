# Experimenting with Similarity Search in a Vector DB

The following generations were conducted with and without using similarity search on the Vector DB. 
1. [Clinical Note Generation](#clinical-note-generation)
2. 

## Clinical Note Generation

The Anthropic Claude v3 Sonnet model was asked to generate a clinical note based on a [sample clinical note](./sample_responses/clinical-notes-01.txt). 

### With embedding and selection

With embedding and selection of the 20 most relevant rows from the csv file, the model does not have a lot of data to work with (since those 20 most relevant rows are very similar). 

View one of the better textual responses here: [attempt-8](./results/clinical-notes-01/attempt-8.txt)

View one of the better JSON responses here (the JSON is cut off due to the token limit set): [attempt-10](./results/clinical-notes-01/attempt-10.txt)

### Using the entire csv file

When generated in textual format, the model seems to be able to summarize the provided csv file to produce a concise clinical note. See [control-attempt-3](./results/clinical-notes-01/control-attempt-3.txt). 

However, in JSON, the model only regurgitates some of the phrases provided to it. See [control-attempt-4](./results/clinical-notes-01/control-attempt-4s.txt)

### Issues with both Methods

1. When the sample response is placed in front of the data provided, the model interprets the sample clinical note as data (i.e. information from the sample is included in the generated clinical note). This may be because the sample clinical note is in JSON. 

2. The model does not use JSON format even though that is specified in the prompt to follow that of the sample (which is in JSON)
    - It only uses JSON format even when specifically prompted to output in JSON. 

3. The JSON output does not summarize the provided input. It is largely a copy-and-paste of some chunks of the textual data provided. 

### Transferable Takeaways

The model places greater emphasis on the first tokens passed to it, even though the maximum size of a payload is technically 20Mb (see [Claude documentation on AWS](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-anthropic-claude-messages.html)). 

### Recommendations

- Can consider having the sample clinical note / referral letter be in continuous text format, since that is what the model expects
- Pass the sample response after the data to minimize the model's incorporation of data from the sample response into the final output