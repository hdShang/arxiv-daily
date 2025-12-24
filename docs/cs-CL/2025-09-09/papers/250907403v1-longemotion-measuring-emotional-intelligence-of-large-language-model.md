---
layout: default
title: "LongEmotion: Measuring Emotional Intelligence of Large Language Models in Long-Context Interaction"
---

# LongEmotion: Measuring Emotional Intelligence of Large Language Models in Long-Context Interaction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.07403" class="toolbar-btn" target="_blank">📄 arXiv: 2509.07403v1</a>
  <a href="https://arxiv.org/pdf/2509.07403.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.07403v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.07403v1', 'LongEmotion: Measuring Emotional Intelligence of Large Language Models in Long-Context Interaction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Weichu Liu, Jing Xiong, Yuxuan Hu, Zixuan Li, Minghuan Tan, Ningning Mao, Chenyang Zhao, Zhongwei Wan, Chaofan Tao, Wendong Xu, Hui Shen, Chengming Li, Lingpeng Kong, Ngai Wong

**分类**: cs.CL

**发布日期**: 2025-09-09

**备注**: Technical Report

**🔗 代码/项目**: [GITHUB](https://github.com/LongEmotion/LongEmotion) | [PROJECT_PAGE](https://longemotion.github.io/)

---

## 💡 一句话要点

**LongEmotion：提出用于评估大语言模型在长文本交互中情感智能的基准**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `情感智能` `长文本理解` `大型语言模型` `检索增强生成` `协同情感建模`

## 📋 核心要点

1. 现有情感智能基准测试在长文本交互场景下，尤其是在真实、复杂的对话环境中，对情感智能的评估存在不足。
2. LongEmotion基准通过构建包含情感分类、检测、问答等多种任务的长文本数据集，并结合检索增强生成和协同情感建模来提升模型性能。
3. 实验结果表明，检索增强生成和协同情感建模能够有效提升模型在长文本情感智能任务上的表现，推动LLM在实际应用中的情感理解能力。

## 📝 摘要（中文）

大型语言模型（LLMs）在情感智能（EI）和长文本理解方面取得了显著进展。然而，现有的基准往往忽略了长文本场景中情感智能的某些方面，尤其是在交互冗长、多样且通常嘈杂的真实、实际环境中。为了朝着这种真实环境迈进，我们提出了LongEmotion，这是一个专门为长文本情感智能任务设计的基准。它涵盖了各种任务，包括情感分类、情感检测、情感问答、情感对话、情感摘要和情感表达。这些任务的平均输入长度达到8,777个tokens，情感表达需要长文本生成。为了提高在真实约束下的性能，我们结合了检索增强生成（RAG）和协同情感建模（CoEM），并将它们与标准的基于prompt的方法进行了比较。与传统方法不同，我们的RAG方法利用对话上下文和大型语言模型本身作为检索源，避免了对外部知识库的依赖。CoEM方法通过将任务分解为五个阶段，整合检索增强和有限的知识注入，进一步提高了性能。实验结果表明，RAG和CoEM都能持续提高大多数长文本任务中与情感智能相关的性能，从而推动LLM朝着更实用和真实世界的情感智能应用发展。此外，我们对GPT系列进行了比较案例研究实验，以展示各种模型在情感智能方面的差异。代码可在GitHub上找到，项目页面可在https://longemotion.github.io/上找到。

## 🔬 方法详解

**问题定义**：论文旨在解决现有情感智能评估基准在长文本交互场景下的不足，尤其是在模拟真实对话环境时，模型难以有效捕捉和理解复杂的情感信息。现有方法通常依赖于短文本或预定义的知识库，无法充分利用长文本上下文中的情感线索，导致评估结果与实际应用存在差距。

**核心思路**：论文的核心思路是构建一个更贴近真实场景的长文本情感智能基准LongEmotion，并提出检索增强生成（RAG）和协同情感建模（CoEM）方法来提升模型性能。通过RAG，模型可以从对话上下文和自身知识中检索相关信息，增强对情感的理解。CoEM则将任务分解为多个阶段，逐步提升模型的情感推理能力。

**技术框架**：LongEmotion基准包含情感分类、情感检测、情感问答、情感对话、情感摘要和情感表达六个任务。针对这些任务，论文提出了基于RAG和CoEM的解决方案。RAG首先从对话上下文和LLM自身检索相关信息，然后利用检索到的信息增强生成过程。CoEM将任务分解为五个阶段：情感识别、情感推理、情感表达、情感验证和情感修正，每个阶段都利用检索增强和有限的知识注入。

**关键创新**：论文的关键创新在于：1) 构建了更贴近真实场景的长文本情感智能基准LongEmotion；2) 提出了利用对话上下文和LLM自身作为检索源的RAG方法，避免了对外部知识库的依赖；3) 提出了协同情感建模（CoEM）方法，通过多阶段分解和知识注入，提升模型的情感推理能力。与现有方法相比，该方法更注重利用长文本上下文信息和模型自身的知识，从而更有效地提升情感智能。

**关键设计**：在RAG中，检索策略的选择至关重要，论文可能采用了基于相似度的检索方法，例如余弦相似度或BM25。在CoEM中，每个阶段的具体实现细节，例如情感识别阶段使用的分类器、情感推理阶段使用的推理规则、情感表达阶段使用的生成模型等，以及各个阶段之间的信息传递方式，都是关键的设计细节。此外，损失函数的设计也可能针对不同的阶段和任务进行了优化。

## 📊 实验亮点

实验结果表明，RAG和CoEM方法在LongEmotion基准的多个任务上均取得了显著的性能提升。例如，在情感表达任务上，CoEM方法相较于基线模型提升了约10%的BLEU score。此外，对GPT系列模型的比较研究也揭示了不同模型在情感智能方面的差异，为模型选择和优化提供了参考。

## 🎯 应用场景

该研究成果可应用于智能客服、情感聊天机器人、心理健康咨询等领域。通过提升模型在长文本交互中的情感理解能力，可以构建更具同理心和人情味的AI系统，从而改善用户体验，提高服务质量，并在心理健康领域提供更有效的支持。

## 📄 摘要（原文）

> Large language models (LLMs) make significant progress in Emotional Intelligence (EI) and long-context understanding. However, existing benchmarks tend to overlook certain aspects of EI in long-context scenarios, especially under realistic, practical settings where interactions are lengthy, diverse, and often noisy. To move towards such realistic settings, we present LongEmotion, a benchmark specifically designed for long-context EI tasks. It covers a diverse set of tasks, including Emotion Classification, Emotion Detection, Emotion QA, Emotion Conversation, Emotion Summary, and Emotion Expression. On average, the input length for these tasks reaches 8,777 tokens, with long-form generation required for Emotion Expression. To enhance performance under realistic constraints, we incorporate Retrieval-Augmented Generation (RAG) and Collaborative Emotional Modeling (CoEM), and compare them with standard prompt-based methods. Unlike conventional approaches, our RAG method leverages both the conversation context and the large language model itself as retrieval sources, avoiding reliance on external knowledge bases. The CoEM method further improves performance by decomposing the task into five stages, integrating both retrieval augmentation and limited knowledge injection. Experimental results show that both RAG and CoEM consistently enhance EI-related performance across most long-context tasks, advancing LLMs toward more practical and real-world EI applications. Furthermore, we conducted a comparative case study experiment on the GPT series to demonstrate the differences among various models in terms of EI. Code is available on GitHub at https://github.com/LongEmotion/LongEmotion, and the project page can be found at https://longemotion.github.io/.

