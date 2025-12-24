---
layout: default
title: "Delta Activations: A Representation for Finetuned Large Language Models"
---

# Delta Activations: A Representation for Finetuned Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.04442" class="toolbar-btn" target="_blank">📄 arXiv: 2509.04442v1</a>
  <a href="https://arxiv.org/pdf/2509.04442.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.04442v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.04442v1', 'Delta Activations: A Representation for Finetuned Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhiqiu Xu, Amish Sethi, Mayur Naik, Ser-Nam Lim

**分类**: cs.LG, cs.AI, cs.CL, cs.IR

**发布日期**: 2025-09-04

**🔗 代码/项目**: [GITHUB](https://github.com/OscarXZQ/delta_activations)

---

## 💡 一句话要点

**提出Delta Activations，通过激活值变化表征微调后的大语言模型，实现模型聚类、选择与合并。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `微调` `模型表示` `激活值` `模型聚类` `模型选择` `模型合并` `向量嵌入`

## 📋 核心要点

1. 现有微调模型元数据不一致，存储库结构化程度低，难以有效导航和理解。
2. 提出Delta Activations，通过测量微调模型与基础模型激活值的变化来表征模型。
3. 实验表明，Delta Activations在模型聚类、选择和合并方面表现出良好的性能和鲁棒性。

## 📝 摘要（中文）

大型开源语言模型（LLMs）的成功使得社区能够创建大量针对特定任务和领域进行后训练的模型。然而，由于元数据不一致和存储库结构化程度低，导航和理解这些模型仍然具有挑战性。我们引入Delta Activations，这是一种通过测量微调模型相对于基础模型内部激活值的变化，将微调模型表示为向量嵌入的方法。这种表示能够有效地按领域和任务进行聚类，从而揭示模型格局的结构。Delta Activations还表现出理想的属性：它在不同的微调设置中具有鲁棒性，并且在混合微调数据集时表现出可加性。此外，我们展示了Delta Activations可以通过少样本微调嵌入任务，并进一步探索其在模型选择和合并中的应用。我们希望Delta Activations能够促进公共可用模型的重用。

## 🔬 方法详解

**问题定义**：论文旨在解决如何有效表示和理解大量微调后的大语言模型的问题。现有方法主要依赖于模型的元数据，但这些元数据往往不一致或不完整，导致难以对模型进行有效的组织、检索和重用。因此，需要一种能够捕捉模型内在特征的表示方法，以便更好地理解和利用这些模型。

**核心思路**：论文的核心思路是通过测量微调后模型内部激活值的变化来表征模型。这种方法基于一个假设：微调过程会对模型的内部表示产生影响，而这些影响可以通过激活值的变化来捕捉。通过将这些变化编码成向量嵌入，可以实现对模型的有效表示和比较。

**技术框架**：Delta Activations 的技术框架主要包含以下几个步骤：1. 选择一个基础模型（base model）。2. 对基础模型进行微调，得到微调后的模型（finetuned model）。3. 选择模型中的若干层，提取基础模型和微调模型在这些层上的激活值。4. 计算微调模型相对于基础模型的激活值变化（delta activations）。5. 将这些变化编码成向量嵌入，作为模型的表示。

**关键创新**：该方法最重要的创新点在于使用激活值的变化来表征微调后的模型。与直接使用模型参数或输出结果相比，激活值能够更深入地反映模型的内部表示和学习到的知识。此外，Delta Activations 还具有可加性，这意味着可以通过组合不同数据集上的 Delta Activations 来模拟在混合数据集上进行微调的效果。

**关键设计**：论文的关键设计包括：1. 选择哪些层来提取激活值：论文实验中选择了Transformer模型的中间层。2. 如何计算激活值的变化：论文使用了简单的减法操作。3. 如何将激活值的变化编码成向量嵌入：论文使用了平均池化操作。4. 损失函数：论文主要关注模型表示，没有涉及特定的损失函数设计。

## 📊 实验亮点

论文实验表明，Delta Activations 能够有效地对微调模型进行聚类，区分不同领域和任务的模型。此外，该方法还表现出良好的鲁棒性，在不同的微调设置下都能产生稳定的表示。通过模型选择和合并实验，验证了 Delta Activations 在实际应用中的有效性。代码已开源。

## 🎯 应用场景

Delta Activations 可用于构建更智能的模型存储库，方便用户根据任务需求快速找到合适的预训练模型。此外，该方法还可以应用于模型融合，通过组合不同模型的 Delta Activations 来创建性能更优的模型。在实际应用中，可以帮助开发者更有效地利用现有的预训练模型资源，降低模型开发成本。

## 📄 摘要（原文）

> The success of powerful open source Large Language Models (LLMs) has enabled the community to create a vast collection of post-trained models adapted to specific tasks and domains. However, navigating and understanding these models remains challenging due to inconsistent metadata and unstructured repositories. We introduce Delta Activations, a method to represent finetuned models as vector embeddings by measuring shifts in their internal activations relative to a base model. This representation allows for effective clustering by domain and task, revealing structure in the model landscape. Delta Activations also demonstrate desirable properties: it is robust across finetuning settings and exhibits an additive property when finetuning datasets are mixed. In addition, we show that Delta Activations can embed tasks via few-shot finetuning, and further explore its use for model selection and merging. We hope Delta Activations can facilitate the practice of reusing publicly available models. Code is available at https://github.com/OscarXZQ/delta_activations.

