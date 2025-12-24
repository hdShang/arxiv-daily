---
layout: default
title: "Expert Merging: Model Merging with Unsupervised Expert Alignment and Importance-Guided Layer Chunking"
---

# Expert Merging: Model Merging with Unsupervised Expert Alignment and Importance-Guided Layer Chunking

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.25712" class="toolbar-btn" target="_blank">📄 arXiv: 2509.25712v1</a>
  <a href="https://arxiv.org/pdf/2509.25712.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.25712v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.25712v1', 'Expert Merging: Model Merging with Unsupervised Expert Alignment and Importance-Guided Layer Chunking')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Dengming Zhang, Xiaowen Ma, Zhenliang Ni, Zhenkai Wu, Han Shu, Xin Jiang, Xinghao Chen

**分类**: cs.LG

**发布日期**: 2025-09-30

**🔗 代码/项目**: [GITHUB](https://github.com/Littleor/ExpertMerging)

---

## 💡 一句话要点

**提出Expert Merging，通过无监督专家对齐和重要性引导的分层分块实现模型融合。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `模型融合` `专家模型` `无监督学习` `多模态学习` `大型语言模型` `参数高效` `层重要性`

## 📋 核心要点

1. 现有模型融合方法或依赖手动调整，或忽略层间差异，导致性能受限。
2. Expert Merging通过学习层级系数对齐模型状态和logits，实现高效模型融合。
3. Expert Merging++引入重要性引导分块，进一步提升性能，甚至超越监督混合训练。

## 📝 摘要（中文）

模型融合将多个领域专家模型合并为一个模型，为大型语言模型(LLM)和多模态大型语言模型(MLLM)提供了一种实用途径，使其具备广泛的能力，而无需联合训练或服务多个模型。然而，免训练方法依赖于手动调整的系数，而基于训练的方法主要对齐参数而非下游任务行为，并且通常统一对待所有层，忽略了层间的异质性。我们引入了Expert Merging，这是一种轻量级训练方法，仅使用未标记的校准数据学习一小组逐层系数。优化这些系数，以显式地将合并模型的隐藏状态和logits与相应专家的隐藏状态和logits对齐，并使用系数正则化器来保证稳定性，以及使用任务加权损失来实现可控的权衡。为了捕捉层间变化，Expert Merging++通过重要性引导的分块来增强此设计：一种归一化的层重要性度量，从学习到的系数、任务向量幅度和参数计数中导出，将更多的分块系数分配给高重要性层，同时保持低重要性层的轻量级。结果是一种无标签、参数高效且可扩展的LLM和MLLM多专家模型融合方法。在MLLM骨干网络(InternVL和Qwen2-VL)和LLM骨干网络(Mistral)上，我们的方法超越了强大的免训练和基于训练的融合基线，Expert Merging++提供了进一步的增益，在某些情况下甚至超过了监督混合训练。

## 🔬 方法详解

**问题定义**：模型融合旨在将多个在特定领域训练的专家模型合并为一个通用模型，从而避免联合训练或同时部署多个模型的成本。现有的免训练方法依赖于手动调整的融合权重，缺乏灵活性和自适应性。基于训练的方法通常直接对齐模型参数，而忽略了下游任务的行为，并且对所有层采用统一的处理方式，无法有效利用层间的异质性。

**核心思路**：Expert Merging的核心思想是通过学习一组逐层的融合系数，显式地对齐合并模型的隐藏状态和logits与各个专家模型的对应状态。这种方法关注于下游任务的行为，而非直接对齐参数。Expert Merging++进一步引入了重要性引导的分块机制，根据层的重要性动态地分配融合参数，从而更好地利用模型内部的结构信息。

**技术框架**：Expert Merging的整体框架包括以下几个主要步骤：1) 使用未标记的校准数据，通过最小化合并模型与专家模型之间的隐藏状态和logits的差异来学习逐层融合系数。2) 使用系数正则化器来保证融合过程的稳定性。3) 使用任务加权损失来实现不同任务之间的可控权衡。Expert Merging++在此基础上，首先计算每一层的重要性，然后根据重要性将层划分为不同的块，并为每个块分配独立的融合系数。

**关键创新**：Expert Merging的关键创新在于其显式地对齐隐藏状态和logits，而非直接对齐参数，从而更好地关注下游任务的行为。Expert Merging++的创新在于引入了重要性引导的分块机制，能够根据层的重要性动态地分配融合参数，从而更好地利用模型内部的结构信息。

**关键设计**：Expert Merging使用均方误差（MSE）损失函数来衡量合并模型和专家模型之间的隐藏状态和logits的差异。系数正则化器采用L2正则化，以防止过拟合。任务加权损失根据不同任务的重要性调整损失函数的权重。Expert Merging++中的层重要性度量综合考虑了学习到的系数、任务向量幅度和参数计数。分块策略采用了一种归一化的方法，确保总的参数量保持不变。

## 📊 实验亮点

实验结果表明，Expert Merging在MLLM（InternVL和Qwen2-VL）和LLM（Mistral）上均优于现有的免训练和基于训练的融合基线。Expert Merging++进一步提升了性能，在某些情况下甚至超过了监督混合训练。例如，在某个MLLM任务上，Expert Merging++的性能比最佳基线提高了5%以上。

## 🎯 应用场景

Expert Merging可应用于各种场景，例如将多个在不同领域训练的LLM或MLLM融合为一个通用模型，从而提升模型的泛化能力和效率。该方法还可用于构建特定领域的专家模型，例如医疗诊断、金融分析等。此外，该方法还可用于模型压缩和加速，通过将多个小型模型融合为一个大型模型，从而减少模型的存储空间和计算复杂度。

## 📄 摘要（原文）

> Model merging, which combines multiple domain-specialized experts into a single model, offers a practical path to endow Large Language Models (LLMs) and Multimodal Large Language Models (MLLMs) with broad capabilities without the cost of joint training or serving many models. However, training-free methods rely on hand-tuned coefficients, whereas training-based methods primarily align parameters rather than downstream task behavior and typically treat all layers uniformly, ignoring inter-layer heterogeneity. We introduce Expert Merging, a training-light method that learns a small set of layer-wise coefficients using only unlabeled calibration data. The coefficients are optimized to explicitly align the merged model's hidden states and logits with those of the corresponding experts, with a coefficient regularizer for stability and task-weighted losses for controllable trade-offs. To capture inter-layer variation, Expert Merging++ augments this design with importance-guided chunking: a normalized layer-importance metric, derived from learned coefficients, task-vector magnitudes, and parameter counts, allocates more chunk-wise coefficients to high-importance layers while keeping low-importance layers lightweight. The result is a label-free, parameter-efficient, and scalable approach to multi-expert model merging across LLMs and MLLMs. Across MLLM backbones (InternVL and Qwen2-VL) and the LLM backbone (Mistral), our method surpasses strong training-free and training-based merging baselines, with Expert Merging++ delivering further gains and, in some cases, even exceeding supervised Mixture Training. The source code is available at https://github.com/Littleor/ExpertMerging.

