---
layout: default
title: "BOE-XSUM: Extreme Summarization in Clear Language of Spanish Legal Decrees and Notifications"
---

# BOE-XSUM: Extreme Summarization in Clear Language of Spanish Legal Decrees and Notifications

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.24908" class="toolbar-btn" target="_blank">📄 arXiv: 2509.24908v1</a>
  <a href="https://arxiv.org/pdf/2509.24908.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.24908v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.24908v1', 'BOE-XSUM: Extreme Summarization in Clear Language of Spanish Legal Decrees and Notifications')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Andrés Fernández García, Javier de la Rosa, Julio Gonzalo, Roser Morante, Enrique Amigó, Alejandro Benito-Santos, Jorge Carrillo-de-Albornoz, Víctor Fresno, Adrian Ghajari, Guillermo Marco, Laura Plaza, Eva Sánchez Salido

**分类**: cs.CL

**发布日期**: 2025-09-29

**备注**: Published in SEPLN 2025. 20 pages, 4 figures

---

## 💡 一句话要点

**BOE-XSUM：发布西班牙法律公文的明晰语言极端摘要数据集，并验证LLM微调有效性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `法律文本摘要` `西班牙语` `BOE-XSUM数据集` `大型语言模型` `微调`

## 📋 核心要点

1. 现有方法缺乏对西班牙语法律文档的有效摘要，导致法律信息难以快速获取。
2. 论文核心在于构建高质量的BOE-XSUM数据集，并微调中等规模LLM以生成简洁的法律文本摘要。
3. 实验表明，在BOE-XSUM上微调的BERTIN GPT-J 6B模型，性能显著优于通用零样本模型。

## 📝 摘要（中文）

由于信息过载，简洁地总结长文档的能力在日常生活中变得越来越重要。然而，对于西班牙语文档，特别是在法律领域，非常缺乏此类摘要。本文提出了BOE-XSUM，这是一个精心策划的数据集，包含3648份来自西班牙官方公报（BOE）的文档的简洁、通俗易懂的摘要。数据集中的每个条目都包含一个简短的摘要、原始文本及其文档类型标签。我们评估了在中等规模的大型语言模型（LLM）上进行微调后在BOE-XSUM上的性能，并将它们与零样本设置中的通用生成模型进行比较。结果表明，微调后的模型明显优于非专用模型。值得注意的是，性能最佳的模型——BERTIN GPT-J 6B（32位精度）——比最佳零样本模型DeepSeek-R1的性能提高了24%（准确率分别为41.6%和33.5%）。

## 🔬 方法详解

**问题定义**：论文旨在解决西班牙法律公文摘要的稀缺问题。现有方法难以生成简洁、易懂的西班牙语法律摘要，使得法律专业人士和普通民众难以快速理解法律条文。现有方法在处理长法律文档时，往往无法有效提取关键信息，导致摘要质量不高。

**核心思路**：论文的核心思路是构建一个高质量的西班牙法律公文摘要数据集（BOE-XSUM），并利用该数据集对中等规模的LLM进行微调。通过微调，使模型能够更好地理解法律文本的特点，从而生成更准确、更简洁的摘要。

**技术框架**：该研究的技术框架主要包括两个部分：数据集构建和模型微调。数据集构建部分涉及从西班牙官方公报（BOE）收集法律文档，并人工编写简洁的摘要。模型微调部分则选择中等规模的LLM（如BERTIN GPT-J 6B），并在BOE-XSUM数据集上进行微调。

**关键创新**：该论文的关键创新在于构建了BOE-XSUM数据集，这是一个专门针对西班牙法律公文的摘要数据集。该数据集的规模适中，摘要质量高，为训练和评估西班牙语法律文本摘要模型提供了重要资源。此外，论文还验证了在BOE-XSUM上微调LLM的有效性。

**关键设计**：论文的关键设计包括数据集的构建标准（摘要的简洁性和易懂性），以及模型微调的策略（选择合适的LLM和微调参数）。论文使用了BERTIN GPT-J 6B模型，并采用32位精度进行微调。损失函数和网络结构等技术细节未在摘要中详细说明，属于未知信息。

## 📊 实验亮点

实验结果表明，在BOE-XSUM数据集上微调的BERTIN GPT-J 6B模型，其准确率达到了41.6%，比最佳零样本模型DeepSeek-R1（准确率33.5%）提高了24%。这表明，针对特定领域的数据集进行微调可以显著提高LLM的性能。

## 🎯 应用场景

该研究成果可应用于智能法律咨询、法律信息检索、法律文本简化等领域。通过自动生成法律公文的简洁摘要，可以帮助法律专业人士和普通民众快速了解法律法规的内容，提高法律服务的效率和可及性。未来，该技术还可以扩展到其他语言和法律领域。

## 📄 摘要（原文）

> The ability to summarize long documents succinctly is increasingly important in daily life due to information overload, yet there is a notable lack of such summaries for Spanish documents in general, and in the legal domain in particular. In this work, we present BOE-XSUM, a curated dataset comprising 3,648 concise, plain-language summaries of documents sourced from Spain's ``Boletín Oficial del Estado'' (BOE), the State Official Gazette. Each entry in the dataset includes a short summary, the original text, and its document type label. We evaluate the performance of medium-sized large language models (LLMs) fine-tuned on BOE-XSUM, comparing them to general-purpose generative models in a zero-shot setting. Results show that fine-tuned models significantly outperform their non-specialized counterparts. Notably, the best-performing model -- BERTIN GPT-J 6B (32-bit precision) -- achieves a 24\% performance gain over the top zero-shot model, DeepSeek-R1 (accuracies of 41.6\% vs.\ 33.5\%).

