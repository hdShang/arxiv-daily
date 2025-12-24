---
layout: default
title: "DisCoCLIP: A Distributional Compositional Tensor Network Encoder for Vision-Language Understanding"
---

# DisCoCLIP: A Distributional Compositional Tensor Network Encoder for Vision-Language Understanding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.21287" class="toolbar-btn" target="_blank">📄 arXiv: 2509.21287v1</a>
  <a href="https://arxiv.org/pdf/2509.21287.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.21287v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.21287v1', 'DisCoCLIP: A Distributional Compositional Tensor Network Encoder for Vision-Language Understanding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kin Ian Lo, Hala Hawashin, Mina Abbaszadeh, Tilen Limback-Stokin, Hadi Wazni, Mehrnoosh Sadrzadeh

**分类**: cs.CL, cs.AI

**发布日期**: 2025-09-25

---

## 💡 一句话要点

**DisCoCLIP：一种用于视觉-语言理解的分布组合张量网络编码器**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉-语言理解` `组合推理` `张量网络` `句法结构` `CLIP` `自监督学习` `多模态融合`

## 📋 核心要点

1. 现有视觉-语言模型忽略了语言的组合结构，导致在理解词序和语义关系的任务上表现不佳。
2. DisCoCLIP结合CLIP视觉Transformer和张量网络文本编码器，显式编码句子的句法结构，提升组合推理能力。
3. 实验表明，DisCoCLIP在SVO-Probes、ARO等基准测试中显著提升了性能，验证了其有效性。

## 📝 摘要（中文）

现有的视觉-语言模型擅长大规模图像-文本对齐，但常常忽略语言的组合结构，导致在依赖词序和谓词-论元结构的任务上表现不佳。我们提出了DisCoCLIP，一种多模态编码器，它结合了冻结的CLIP视觉Transformer和一个新颖的张量网络文本编码器，该编码器显式地编码了句法结构。句子通过组合范畴语法解析器进行解析，产生分布式的词张量，其收缩反映了句子的语法推导。为了保持模型的效率，高阶张量通过张量分解进行分解，将参数数量从数千万减少到一百万以下。通过自监督对比损失进行端到端训练，DisCoCLIP显著提高了对动词语义和词序的敏感性：它将CLIP的SVO-Probes动词准确率从77.6%提高到82.4%，将ARO属性和关系分数提高了9%以上和4%，并在新引入的SVO-Swap基准上实现了93.7%的准确率。这些结果表明，通过张量网络嵌入显式的语言结构可以产生可解释的、参数高效的表示，从而显著提高视觉-语言任务中的组合推理能力。

## 🔬 方法详解

**问题定义**：现有视觉-语言模型，如CLIP，在图像-文本对齐方面表现出色，但在理解语言的组合性方面存在不足。它们难以捕捉词序和谓词-论元结构等关键信息，导致在需要复杂推理的任务中表现下降。现有方法缺乏对语言结构的显式建模，是其痛点所在。

**核心思路**：DisCoCLIP的核心思路是将句子的句法结构显式地编码到文本表示中。通过使用组合范畴语法（CCG）解析器解析句子，并将每个词表示为分布式的张量，张量的收缩过程模拟了句子的语法推导过程。这种设计使得模型能够更好地理解词与词之间的关系，从而提高组合推理能力。

**技术框架**：DisCoCLIP的整体架构包括一个冻结的CLIP视觉Transformer和一个张量网络文本编码器。首先，图像通过CLIP视觉Transformer提取视觉特征。然后，句子通过CCG解析器进行解析，生成句法树。每个词被表示为一个张量，并通过张量收缩操作将句法树的信息编码到句子的表示中。最后，使用自监督对比损失进行端到端训练，使视觉和语言表示对齐。

**关键创新**：DisCoCLIP最重要的创新点在于使用张量网络来显式地编码句子的句法结构。与传统的文本编码器相比，张量网络能够更好地捕捉词与词之间的关系，从而提高组合推理能力。此外，为了提高模型的效率，DisCoCLIP使用了张量分解技术，减少了参数数量。

**关键设计**：DisCoCLIP的关键设计包括：1) 使用CCG解析器生成句法树；2) 将每个词表示为一个张量，张量的维度与词的语义和句法角色相关；3) 使用张量收缩操作将句法树的信息编码到句子的表示中；4) 使用张量分解技术减少参数数量；5) 使用自监督对比损失进行端到端训练。

## 📊 实验亮点

DisCoCLIP在多个基准测试中取得了显著的性能提升。在SVO-Probes动词准确率上，DisCoCLIP将CLIP的性能从77.6%提高到82.4%。在ARO属性和关系分数上，DisCoCLIP分别提升了9%以上和4%。此外，DisCoCLIP在SVO-Swap基准上实现了93.7%的准确率，表明其对词序的敏感性显著提高。这些结果表明，DisCoCLIP能够有效地提高视觉-语言模型的组合推理能力。

## 🎯 应用场景

DisCoCLIP的潜在应用领域包括图像描述生成、视觉问答、以及需要理解复杂语言结构的机器人控制等。通过提高模型对语言组合性的理解，可以使机器更好地理解人类的意图，从而实现更自然的人机交互。该研究的实际价值在于提升视觉-语言模型的推理能力，未来可能推动更智能的AI应用。

## 📄 摘要（原文）

> Recent vision-language models excel at large-scale image-text alignment but often neglect the compositional structure of language, leading to failures on tasks that hinge on word order and predicate-argument structure. We introduce DisCoCLIP, a multimodal encoder that combines a frozen CLIP vision transformer with a novel tensor network text encoder that explicitly encodes syntactic structure. Sentences are parsed with a Combinatory Categorial Grammar parser to yield distributional word tensors whose contractions mirror the sentence's grammatical derivation. To keep the model efficient, high-order tensors are factorized with tensor decompositions, reducing parameter count from tens of millions to under one million. Trained end-to-end with a self-supervised contrastive loss, DisCoCLIP markedly improves sensitivity to verb semantics and word order: it raises CLIP's SVO-Probes verb accuracy from 77.6% to 82.4%, boosts ARO attribution and relation scores by over 9% and 4%, and achieves 93.7% on a newly introduced SVO-Swap benchmark. These results demonstrate that embedding explicit linguistic structure via tensor networks yields interpretable, parameter-efficient representations that substantially improve compositional reasoning in vision-language tasks.

