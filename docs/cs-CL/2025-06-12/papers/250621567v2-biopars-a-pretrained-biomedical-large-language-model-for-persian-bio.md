---
layout: default
title: "BioPars: A Pretrained Biomedical Large Language Model for Persian Biomedical Text Mining"
---

# BioPars: A Pretrained Biomedical Large Language Model for Persian Biomedical Text Mining

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.21567" class="toolbar-btn" target="_blank">📄 arXiv: 2506.21567v2</a>
  <a href="https://arxiv.org/pdf/2506.21567.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.21567v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.21567v2', 'BioPars: A Pretrained Biomedical Large Language Model for Persian Biomedical Text Mining')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Baqer M. Merzah, Tania Taami, Salman Asoudeh, Saeed Mirzaee, Amir reza Hossein pour, Amir Ali Bengari

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-06-12 (更新: 2025-07-01)

**🔗 代码/项目**: [GITHUB](https://github.com/amirap80/BioPars)

---

## 💡 一句话要点

**提出BioPars以解决波斯语生物医学文本挖掘问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `生物医学文本挖掘` `大型语言模型` `波斯语医学问答` `知识获取` `模型评估`

## 📋 核心要点

1. 现有的LLMs在处理波斯语医学文本时存在知识获取和推理能力不足的问题。
2. 论文提出BioPars，通过BIOPARS-BENCH数据集和BioParsQA评估模型，旨在提升波斯语医学问答的生成能力。
3. 实验结果显示，BioPars在多个医学问答数据集上表现优异，ROUGE-L得分和BERTScore均高于现有模型。

## 📝 摘要（中文）

大型语言模型（LLMs）在生命科学领域因其建模、提取和应用复杂生物信息的能力而受到关注。本文首先介绍了BIOPARS-BENCH数据集，该数据集来自超过10,000篇科学文章、教科书和医学网站。随后，提出了BioPars，一个旨在评估LLMs在获取特定领域知识、解释和综合知识及展示证据能力的模型。通过与ChatGPT、Llama和Galactica的比较，研究揭示了这些模型在处理高层次实际问题和细致推理方面的不足。BioPars在波斯语医学问答生成方面表现出色，ROUGE-L得分为29.99，优于GPT-4 1.0，且BERTScore达到90.87。

## 🔬 方法详解

**问题定义**：本文旨在解决波斯语生物医学文本挖掘中的知识获取和推理能力不足的问题。现有的LLMs在处理复杂的医学问答时表现不佳，尤其是在生成长答案方面。

**核心思路**：BioPars通过引入BIOPARS-BENCH数据集和BioParsQA评估标准，专注于提升模型在特定领域知识的获取、解释和综合能力。设计上强调了对波斯语医学文本的适应性。

**技术框架**：整体架构包括数据集构建、模型训练和评估三个主要模块。数据集构建阶段整合了科学文章和医学网站的信息，模型训练阶段使用LLMs进行知识学习，评估阶段则通过BioParsQA进行性能测试。

**关键创新**：BioPars是首个针对波斯语医学问答的LLM应用，特别是在生成长答案方面具有显著优势。与现有模型相比，BioPars在特定领域知识的获取和推理能力上有了实质性提升。

**关键设计**：模型采用了先进的损失函数和网络结构，参数设置经过精细调整，以确保在波斯语医学文本上的最佳表现。具体的技术细节包括使用MMR方法优化BERTScore和其他评估指标。

## 📊 实验亮点

BioPars在BioParsQA数据集上的ROUGE-L得分为29.99，显著优于GPT-4 1.0。同时，模型的BERTScore达到了90.87，MoverScore和BLEURT值也高于其他三种对比模型，显示出其在波斯语医学问答生成中的卓越性能。

## 🎯 应用场景

BioPars的研究成果在医学问答系统、临床决策支持和生物信息学等领域具有广泛的应用潜力。通过提高波斯语医学文本的处理能力，BioPars可以帮助医疗专业人员更有效地获取和应用生物医学知识，推动相关领域的研究和实践发展。

## 📄 摘要（原文）

> Large Language Models (LLMs) have recently gained attention in the life sciences due to their capacity to model, extract, and apply complex biological information. Beyond their classical use as chatbots, these systems are increasingly used for complex analysis and problem-solving in specialized fields, including bioinformatics. First, we introduce BIOPARS-BENCH, a dataset from over 10,000 scientific articles, textbooks, and medical websites. BioParsQA was also introduced to evaluate the proposed model, which consists of 5,231 Persian medical questions and answers. This study then introduces BioPars, a simple but accurate measure designed to assess LLMs for three main abilities: acquiring subject-specific knowledge, interpreting and synthesizing such knowledge, and demonstrating proper evidence. Comparing ChatGPT, Llama, and Galactica, our study highlights their ability to remember and retrieve learned knowledge but also reveals shortcomings in addressing higher-level, real-world questions and fine-grained inferences. These findings indicate the need for further fine-tuning to address the capabilities of LLM in bioinformatics tasks. To our knowledge, BioPars is the first application of LLM in Persian medical QA, especially for generating long answers. Evaluation of four selected medical QA datasets shows that BioPars has achieved remarkable results compared to comparative approaches. The model on BioParsQA achieved a ROUGE-L score of 29.99, which is an improvement over GPT-4 1.0. The model achieved a BERTScore of 90.87 with the MMR method. The MoverScore and BLEURT values were also higher in this model than the other three models. In addition, the reported scores for the model are MoverScore=60.43 and BLEURT=50.78. BioPars is an ongoing project and all resources related to its development will be made available via the following GitHub repository: https://github.com/amirap80/BioPars.

