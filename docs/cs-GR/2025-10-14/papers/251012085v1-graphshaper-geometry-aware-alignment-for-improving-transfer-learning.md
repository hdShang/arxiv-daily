---
layout: default
title: GraphShaper: Geometry-aware Alignment for Improving Transfer Learning in Text-Attributed Graphs
---

# GraphShaper: Geometry-aware Alignment for Improving Transfer Learning in Text-Attributed Graphs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.12085" class="toolbar-btn" target="_blank">📄 arXiv: 2510.12085v1</a>
  <a href="https://arxiv.org/pdf/2510.12085.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.12085v1" onclick="toggleFavorite(this, '2510.12085v1', 'GraphShaper: Geometry-aware Alignment for Improving Transfer Learning in Text-Attributed Graphs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Heng Zhang, Tianyi Zhang, Yuling Shi, Xiaodong Gu, Yaomin Shen, Haochen You, Zijian Zhang, Yilei Yuan, Jin Huang

**分类**: cs.LG, cs.GR

**发布日期**: 2025-10-14

---

## 💡 一句话要点

**GraphShaper提出几何感知对齐框架，提升文本属性图的迁移学习性能。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `图神经网络` `几何深度学习` `迁移学习` `对比学习` `图文对齐`

## 📋 核心要点

1. 现有图学习方法假设图结构可统一编码在欧几里得空间，忽略了图结构内在的几何多样性，导致结构边界性能下降。
2. GraphShaper提出几何感知对齐框架，通过多几何专家网络自适应融合不同几何属性，保持结构完整性。
3. 实验表明，GraphShaper在引文网络和社交网络零样本学习中，准确率分别提升9.47%和7.63%。

## 📝 摘要（中文）

图基础模型代表了一种变革性的范式，用于学习跨不同图域的可迁移表示。最近的方法利用大型语言模型，通过对比学习将图和文本模态统一到共享的表示空间中。然而，系统评估表明，在不同的拓扑模式汇聚的结构边界处，性能显著下降，准确率损失超过20个百分点。这个问题源于一个关键的局限性：当前的方法假设所有图结构都可以编码在单个欧几里得空间中。实际上，树结构需要双曲几何来保持分层分支，而循环模式依赖于球面几何来实现闭合特性。在结构边界处，节点会遇到统一编码空间无法解决的冲突几何约束。这提出了一个关键挑战：是否可以设计对齐框架来尊重图结构的内在几何多样性？我们引入了GraphShaper，这是一个几何感知框架，通过多几何专业化来增强图编码。我们的方法采用针对不同几何空间定制的专家网络，动态计算融合权重，以自适应地整合基于局部结构特征的几何属性。这种自适应融合在与文本嵌入对齐之前保持了结构完整性。大量实验表明，GraphShaper在零样本设置下，在引文网络上实现了9.47%的准确率提升，在社交网络上实现了7.63%的准确率提升。

## 🔬 方法详解

**问题定义**：论文旨在解决现有图学习方法在处理具有复杂结构（如树形和环形结构混合）的图数据时，由于忽略了不同结构内在的几何特性，导致在结构边界处性能显著下降的问题。现有方法通常假设所有图结构都可以编码在单一的欧几里得空间中，这与实际情况不符，因为树形结构更适合用双曲几何表示，而环形结构更适合用球面几何表示。

**核心思路**：论文的核心思路是设计一个几何感知的对齐框架，该框架能够根据图的局部结构特征，自适应地选择合适的几何空间进行编码，从而更好地保留图结构的内在几何特性。通过这种方式，可以缓解在结构边界处由于几何约束冲突而导致的性能下降问题。

**技术框架**：GraphShaper框架主要包含以下几个模块：1) 局部结构分析模块：用于分析图中节点的局部结构特征，例如节点的度、聚类系数等。2) 几何专家网络模块：包含多个针对不同几何空间（如欧几里得空间、双曲空间、球面空间）的专家网络，每个专家网络负责学习在特定几何空间下的图节点表示。3) 几何融合模块：根据局部结构分析的结果，动态计算每个几何专家网络的融合权重，并将不同几何空间下的节点表示进行融合，得到最终的节点表示。4) 对齐模块：将融合后的图节点表示与文本嵌入进行对齐，从而实现图和文本模态的统一表示。

**关键创新**：GraphShaper的关键创新在于其几何感知的自适应融合机制。与现有方法不同，GraphShaper不是简单地将所有图结构编码到单一的欧几里得空间中，而是根据图的局部结构特征，自适应地选择合适的几何空间进行编码。这种自适应融合机制能够更好地保留图结构的内在几何特性，从而提高图学习的性能。

**关键设计**：在几何融合模块中，论文使用了一种基于注意力机制的融合方法。具体来说，首先将局部结构分析的结果作为查询向量，然后将每个几何专家网络的输出作为键值对，通过注意力机制计算每个几何专家网络的融合权重。此外，论文还设计了一种对比学习损失函数，用于对齐图节点表示和文本嵌入。损失函数的目标是使相似的图节点和文本嵌入在表示空间中更加接近，而不相似的图节点和文本嵌入在表示空间中更加远离。

## 📊 实验亮点

实验结果表明，GraphShaper在引文网络（Cora、Citeseer、Pubmed）和社交网络（ogbn-arxiv）上均取得了显著的性能提升。在零样本学习设置下，GraphShaper在引文网络上实现了平均9.47%的准确率提升，在社交网络上实现了7.63%的准确率提升。这些结果表明，GraphShaper能够有效地利用图结构的几何信息，提高图表示学习的性能。

## 🎯 应用场景

GraphShaper在图表示学习领域具有广泛的应用前景，例如社交网络分析、知识图谱推理、推荐系统等。通过更好地捕捉图结构的内在几何特性，GraphShaper可以提高这些应用场景下的性能。此外，该方法还可以应用于其他类型的图数据，例如生物网络、化学分子图等，具有很高的实际价值和未来影响。

## 📄 摘要（原文）

> Graph foundation models represent a transformative paradigm for learning transferable representations across diverse graph domains. Recent methods leverage large language models to unify graph and text modalities into a shared representation space using contrastive learning. However, systematic evaluations reveal significant performance degradation at structural boundaries where distinct topological patterns converge, with accuracy losses exceeding 20 percentage points. This issue arises from a key limitation: current methods assume all graph structures can be encoded within a single Euclidean space. In reality, tree structures require hyperbolic geometry to preserve hierarchical branching, while cyclic patterns depend on spherical geometry for closure properties. At structural boundaries, nodes experience conflicting geometric constraints that uniform encoding spaces cannot resolve. This raises a crucial challenge: \textbf{Can alignment frameworks be designed to respect the intrinsic geometric diversity of graph structures?} We introduce \textbf{GraphShaper}, a geometry-aware framework that enhances graph encoding through multi-geometric specialization. Our approach employs expert networks tailored to different geometric spaces, dynamically computing fusion weights to adaptively integrate geometric properties based on local structural characteristics. This adaptive fusion preserves structural integrity before alignment with text embeddings. Extensive experiments demonstrate that GraphShaper achieves 9.47\% accuracy improvements on citation networks and 7.63\% on social networks in zero-shot settings.

