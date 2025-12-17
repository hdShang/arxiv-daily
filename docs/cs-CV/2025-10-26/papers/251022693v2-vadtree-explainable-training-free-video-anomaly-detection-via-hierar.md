---
layout: default
title: VADTree: Explainable Training-Free Video Anomaly Detection via Hierarchical Granularity-Aware Tree
---

# VADTree: Explainable Training-Free Video Anomaly Detection via Hierarchical Granularity-Aware Tree

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.22693" class="toolbar-btn" target="_blank">📄 arXiv: 2510.22693v2</a>
  <a href="https://arxiv.org/pdf/2510.22693.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.22693v2" onclick="toggleFavorite(this, '2510.22693v2', 'VADTree: Explainable Training-Free Video Anomaly Detection via Hierarchical Granularity-Aware Tree')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wenlong Li, Yifei Xu, Yuan Rao, Zhenhua Wang, Shuiguang Deng

**分类**: cs.CV

**发布日期**: 2025-10-26 (更新: 2025-10-28)

**备注**: NeurIPS 2025 poster

**🔗 代码/项目**: [GITHUB](https://github.com/wenlongli10/VADTree)

---

## 💡 一句话要点

**VADTree：通过分层粒度感知树实现可解释的无训练视频异常检测**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视频异常检测` `无训练学习` `分层粒度感知` `事件边界检测` `视觉语言模型`

## 📋 核心要点

1. 现有无训练视频异常检测方法采用固定长度时间窗口采样，难以捕捉不同时间跨度的异常。
2. VADTree利用分层粒度感知树(HGTree)结构，通过自适应粗细粒度分层结构化和冗余消除实现灵活采样。
3. 实验表明，VADTree在无训练设置中取得了SOTA性能，并显著减少了采样片段数量。

## 📝 摘要（中文）

视频异常检测(VAD)旨在识别视频中的异常事件。有监督方法需要大量的领域内训练数据，并且无法为异常提供清晰的解释。相比之下，无训练方法利用大型预训练模型的知识储备和语言交互能力来检测异常。然而，当前固定长度的时间窗口采样方法难以准确捕获具有不同时间跨度的异常。因此，我们提出了VADTree，它利用分层粒度感知树(HGTree)结构进行VAD中的灵活采样。VADTree利用预训练的通用事件边界检测(GEBD)模型中嵌入的知识来表征潜在的异常事件边界。具体来说，VADTree基于边界置信度将视频分解为通用事件节点，并执行自适应的粗细粒度分层结构化和冗余消除来构建HGTree。然后，将多维先验注入到视觉语言模型(VLM)中，以增强节点级的异常感知，并通过大型语言模型(LLM)实现通用事件节点的异常推理。最后，使用一种集群间节点相关方法来整合多粒度异常分数。在三个具有挑战性的数据集上的大量实验表明，VADTree在无训练设置中实现了最先进的性能，同时大大减少了采样的视频片段数量。代码将在https://github.com/wenlongli10/VADTree上提供。

## 🔬 方法详解

**问题定义**：论文旨在解决无训练视频异常检测中，现有方法无法有效处理不同时间跨度异常的问题。现有方法通常采用固定长度的时间窗口进行采样，这导致对于时间跨度较短或较长的异常事件难以准确捕捉，从而影响检测性能。此外，现有方法缺乏对异常事件的有效解释。

**核心思路**：论文的核心思路是构建一个分层粒度感知树(HGTree)，该树结构能够自适应地对视频进行粗细粒度的划分，从而灵活地捕捉不同时间跨度的异常事件。通过利用预训练的通用事件边界检测模型，可以有效地识别潜在的异常事件边界，并以此为基础构建HGTree。同时，结合视觉语言模型和大型语言模型，实现对异常事件的感知和推理。

**技术框架**：VADTree的整体框架主要包含以下几个阶段：
1. **事件边界检测**：利用预训练的GEBD模型检测视频中的事件边界，并计算边界置信度。
2. **HGTree构建**：基于边界置信度将视频分解为通用事件节点，并进行自适应的粗细粒度分层结构化和冗余消除，构建HGTree。
3. **节点异常感知**：将多维先验注入到视觉语言模型(VLM)中，增强节点级的异常感知。
4. **异常推理**：通过大型语言模型(LLM)对通用事件节点进行异常推理。
5. **异常分数整合**：使用集群间节点相关方法整合多粒度异常分数，得到最终的异常检测结果。

**关键创新**：VADTree的关键创新在于提出了分层粒度感知树(HGTree)结构，该结构能够根据视频内容自适应地调整采样粒度，从而更有效地捕捉不同时间跨度的异常事件。与现有方法采用的固定长度时间窗口采样相比，HGTree具有更高的灵活性和适应性。此外，结合视觉语言模型和大型语言模型进行异常感知和推理，提高了异常检测的准确性和可解释性。

**关键设计**：
1. **HGTree的构建**：采用自适应的粗细粒度分层结构化方法，根据事件边界置信度动态调整树的深度和分支。
2. **多维先验注入**：将时间、空间和语义等多维先验信息注入到视觉语言模型中，以增强节点级的异常感知能力。
3. **集群间节点相关方法**：利用节点之间的相关性信息，整合多粒度异常分数，提高检测的鲁棒性。

## 📊 实验亮点

VADTree在三个具有挑战性的数据集上进行了实验，结果表明，在无训练设置下，VADTree取得了state-of-the-art的性能，同时显著减少了采样的视频片段数量。具体性能数据和对比基线需要在论文中查找。该方法在保证检测精度的同时，降低了计算复杂度，具有实际应用价值。

## 🎯 应用场景

VADTree在视频监控、智能交通、工业安全等领域具有广泛的应用前景。它可以用于自动检测监控视频中的异常行为，例如打架斗殴、盗窃等；在智能交通领域，可以用于检测交通事故、车辆违规行为等；在工业安全领域，可以用于检测生产线上的异常操作，保障生产安全。该研究有助于提升视频监控系统的智能化水平，降低人工监控成本，提高安全保障能力。

## 📄 摘要（原文）

> Video anomaly detection (VAD) focuses on identifying anomalies in videos. Supervised methods demand substantial in-domain training data and fail to deliver clear explanations for anomalies. In contrast, training-free methods leverage the knowledge reserves and language interactivity of large pre-trained models to detect anomalies. However, the current fixed-length temporal window sampling approaches struggle to accurately capture anomalies with varying temporal spans. Therefore, we propose VADTree that utilizes a Hierarchical Granularityaware Tree (HGTree) structure for flexible sampling in VAD. VADTree leverages the knowledge embedded in a pre-trained Generic Event Boundary Detection (GEBD) model to characterize potential anomaly event boundaries. Specifically, VADTree decomposes the video into generic event nodes based on boundary confidence, and performs adaptive coarse-fine hierarchical structuring and redundancy removal to construct the HGTree. Then, the multi-dimensional priors are injected into the visual language models (VLMs) to enhance the node-wise anomaly perception, and anomaly reasoning for generic event nodes is achieved via large language models (LLMs). Finally, an inter-cluster node correlation method is used to integrate the multi-granularity anomaly scores. Extensive experiments on three challenging datasets demonstrate that VADTree achieves state-of-the-art performance in training-free settings while drastically reducing the number of sampled video segments. The code will be available at https://github.com/wenlongli10/VADTree.

