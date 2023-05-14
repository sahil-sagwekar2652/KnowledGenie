![Logo](https://media.discordapp.net/attachments/1106591604032147619/1107277394462658610/kg.png?width=1382&height=440)

<p align="center" style="font-size:240px;">
<b>Ask your documents anything. Get answers instantly.</b>
</p>

<p align="center">
  <img src="https://skillicons.dev/icons?i=py,flask,html,css,github">
</p>

<p align="center">
  <img src="https://github.com/sahil-sagwekar2652/ai-hackfest-project/workflows/Flake8Linter/badge.svg">
</p>

  
<!-- [![ai-hackfest-project](https://github-readme-stats.vercel.app/api/pin/?username=sahil-sagwekar2652&repo=ai-hackfest-project&theme=dark)](https://github.com/sahil-sagwekar2652/ai-hackfest-project)<br/> -->

<!-- [![My Skills]()](https://skillicons.dev) -->

- - -

**KnowledGenie**  is a web application that allows users to upload a PDF and ask queries to which answers will be provided along with the reference text. The application uses a large language model (LLM) to process the PDF and generate answers to the user's queries. The LLM is trained on a massive dataset of text and code, which allows it to understand and respond to a wide range of queries.

## How we built it

We built KnowledGenie using LangChain with HuggingFace LLMs. LangChain is a framework that makes it easy to build LLM-powered applications. The Hugging Face Hub is a platform with over 120k models, 20k datasets, and 50k demo apps (Spaces), all open source and publicly available, in an online platform where people can easily collaborate and build ML together.

The model utilized for the retrieval of answers in KnowledGenie is flan-t5-large. This model is a Transformer-based LLM that has been trained on a massive dataset of text and code. The model is able to generate text, translate languages, write different kinds of creative content, and answer your questions in an informative way. In our case, we utilized flan-t5-large to answer queries asked by the user and point to where the answer was picked from in the uploaded document.


