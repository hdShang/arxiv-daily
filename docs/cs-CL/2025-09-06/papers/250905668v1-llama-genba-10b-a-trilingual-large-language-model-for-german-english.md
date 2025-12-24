---
layout: default
title: "Llama-GENBA-10B: A Trilingual Large Language Model for German, English and Bavarian"
---

# Llama-GENBA-10B: A Trilingual Large Language Model for German, English and Bavarian

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.05668" class="toolbar-btn" target="_blank">📄 arXiv: 2509.05668v1</a>
  <a href="https://arxiv.org/pdf/2509.05668.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.05668v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.05668v1', 'Llama-GENBA-10B: A Trilingual Large Language Model for German, English and Bavarian')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Michael Hoffmann, Jophin John, Stefan Schweter, Gokul Ramakrishnan, Hoi-Fong Mak, Alice Zhang, Dmitry Gaynullin, Nicolay J. Hammer

**分类**: cs.CL, cs.AI

**发布日期**: 2025-09-06

**备注**: Michael Hoffmann and Jophin John contributed equally to this work

---

## 💡 一句话要点

**Llama-GENBA-10B：一种用于德语、英语和巴伐利亚语的三语大型语言模型**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多语言模型` `低资源语言` `跨语言迁移` `巴伐利亚语` `大型语言模型`

## 📋 核心要点

1. 现有大型语言模型存在以英语为中心的偏差，忽略了其他语言，尤其对低资源语言支持不足。
2. Llama-GENBA-10B通过平衡英语、德语和巴伐利亚语的预训练数据，并优化模型架构，实现更好的跨语言性能。
3. 实验结果表明，Llama-GENBA-10B在巴伐利亚语上超越现有模型，并在英语和德语上达到或超过现有水平。

## 📝 摘要（中文）

本文介绍了Llama-GENBA-10B，一种旨在解决大型语言模型中以英语为中心的偏差的三语基础模型。Llama-GENBA-10B基于Llama 3.1-8B构建，扩展到100亿参数，并在1640亿tokens上进行持续预训练（820亿英语，820亿德语和8000万巴伐利亚语），在平衡资源的同时防止英语的主导地位。该模型面向德国NLP社区，同时也推广巴伐利亚语这种低资源语言。开发过程解决了四个挑战：（1）在巴伐利亚语稀缺的情况下，管理一个多语语料库；（2）为英语、德语和巴伐利亚语创建一个统一的分词器；（3）优化架构和语言比例超参数以实现跨语言迁移；（4）通过将德国基准翻译成巴伐利亚语，建立第一个标准化的三语评估套件。评估表明，Llama-GENBA-10B实现了强大的跨语言性能，微调后的变体在巴伐利亚语中超过了Apertus-8B-2509和gemma-2-9b，并成为该语言同类最佳模型，同时在英语中优于EuroLLM，并在德语中与其结果相匹配。在Cerebras CS-2上进行的训练证明了高效的大规模多语预训练，并记录了能源使用情况，为整合低资源语言的包容性基础模型提供了蓝图。

## 🔬 方法详解

**问题定义**：现有的大型语言模型通常以英语为中心，导致在其他语言，特别是低资源语言上的表现不佳。这限制了这些模型在多语言环境中的应用，并且可能加剧语言之间的数字鸿沟。现有方法难以平衡不同语言的数据量，并且缺乏针对低资源语言的优化。

**核心思路**：Llama-GENBA-10B的核心思路是通过平衡不同语言的预训练数据，并针对跨语言迁移进行优化，从而构建一个更公平、更高效的多语言模型。该模型特别关注巴伐利亚语，一种低资源语言，旨在提升其在该语言上的性能。

**技术框架**：Llama-GENBA-10B基于Llama 3.1-8B构建，并扩展到100亿参数。该模型在包含英语、德语和巴伐利亚语的1640亿tokens上进行持续预训练。为了评估模型的性能，作者构建了一个标准化的三语评估套件，包括将德国基准翻译成巴伐利亚语。训练过程在Cerebras CS-2上进行。

**关键创新**：该论文的关键创新在于：（1）构建了一个平衡的多语语料库，特别关注低资源语言巴伐利亚语；（2）创建了一个统一的分词器，能够有效处理英语、德语和巴伐利亚语；（3）优化了模型架构和语言比例超参数，以实现更好的跨语言迁移；（4）建立了第一个标准化的三语评估套件。

**关键设计**：模型使用Llama 3.1-8B作为基础模型，并扩展到100亿参数。预训练数据包含820亿英语tokens，820亿德语tokens和8000万巴伐利亚语tokens。作者针对跨语言迁移优化了模型架构和语言比例超参数，但具体细节未知。训练过程在Cerebras CS-2上进行，并记录了能源使用情况。

## 📊 实验亮点

Llama-GENBA-10B在巴伐利亚语上的微调变体超越了Apertus-8B-2509和gemma-2-9b，成为该语言同类最佳模型。同时，该模型在英语上优于EuroLLM，并在德语上与其结果相匹配。这些结果表明，Llama-GENBA-10B在跨语言性能方面具有显著优势。

## 🎯 应用场景

Llama-GENBA-10B的应用场景包括多语言机器翻译、跨语言信息检索、多语言内容生成等。该模型特别适用于需要处理德语、英语和巴伐利亚语的场景。通过提升低资源语言的性能，该研究有助于促进语言多样性和数字包容性，并为其他低资源语言模型的开发提供参考。

## 📄 摘要（原文）

> We present Llama-GENBA-10B, a trilingual foundation model addressing English-centric bias in large language models. Built on Llama 3.1-8B and scaled to 10B parameters, Llama-GENBA-10B is continuously pretrained on 164B tokens (82B English, 82B German, and 80M Bavarian), balancing resources while preventing English dominance. Targeted at the German NLP community, the model also promotes Bavarian as a low-resource language. Development tackled four challenges: (1) curating a multilingual corpus despite Bavarian scarcity, (2) creating a unified tokenizer for English, German, and Bavarian, (3) optimizing architecture and language-ratio hyperparameters for cross-lingual transfer, and (4) establishing the first standardized trilingual evaluation suite by translating German benchmarks into Bavarian. Evaluations show that Llama-GENBA-10B achieves strong cross-lingual performance, with the fine-tuned variant surpassing Apertus-8B-2509 and gemma-2-9b in Bavarian and establishing itself as the best model in its class for this language, while also outperforming EuroLLM in English and matching its results in German. Training on the Cerebras CS-2 demonstrated efficient large-scale multilingual pretraining with documented energy use, offering a blueprint for inclusive foundation models that integrate low-resource languages.

