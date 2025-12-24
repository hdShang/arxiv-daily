---
layout: default
title: "MOL: Joint Estimation of Micro-Expression, Optical Flow, and Landmark via Transformer-Graph-Style Convolution"
---

# MOL: Joint Estimation of Micro-Expression, Optical Flow, and Landmark via Transformer-Graph-Style Convolution

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.14511" class="toolbar-btn" target="_blank">📄 arXiv: 2506.14511v1</a>
  <a href="https://arxiv.org/pdf/2506.14511.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.14511v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.14511v1', 'MOL: Joint Estimation of Micro-Expression, Optical Flow, and Landmark via Transformer-Graph-Style Convolution')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhiwen Shao, Yifan Cheng, Feiran Li, Yong Zhou, Xuequan Lu, Yuan Xie, Lizhuang Ma

**分类**: cs.CV

**发布日期**: 2025-06-17

**备注**: This paper has been accepted by IEEE Transactions on Pattern Analysis and Machine Intelligence

**DOI**: [10.1109/TPAMI.2025.3581162](https://doi.org/10.1109/TPAMI.2025.3581162)

**🔗 代码/项目**: [GITHUB](https://github.com/CYF-cuber/MOL)

---

## 💡 一句话要点

**提出MOL框架以解决微表情识别中的数据不足问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `微表情识别` `深度学习` `变换器` `图卷积` `光流估计` `面部关键点检测` `特征提取` `联合训练`

## 📋 核心要点

1. 微表情识别面临的主要挑战是现有方法依赖于手工特征和有限的数据集，导致性能受限。
2. 本文提出了一种新颖的深度学习框架，结合变换器和图卷积，能够直接从原始帧中提取特征，避免了对关键帧的依赖。
3. 实验结果显示，该框架在CASME II、SAMM和SMIC基准上超越了现有最先进的MER方法，并有效捕捉面部微小肌肉动作。

## 📝 摘要（中文）

微表情识别（MER）是一项具有挑战性的任务，主要由于微表情动作的瞬时性和细微性。现有方法通常依赖于手工特征、关键帧或受限于小规模和低多样性数据集的深度网络。本文提出了一种端到端的微动作感知深度学习框架，结合了变换器、图卷积和传统卷积的优势。特别地，提出了一种新颖的F5C模块，由全连接卷积和通道对应卷积组成，能够直接从原始帧序列中提取局部和全局特征，而无需关键帧的先验知识。通过共享局部-全局特征，MER、光流估计和面部关键点检测共同训练，从而捕捉面部微妙动作信息，缓解训练数据不足的影响。实验表明，该框架在多个基准上超越了现有的MER方法，并在光流估计和面部关键点检测方面表现良好。

## 🔬 方法详解

**问题定义**：本文旨在解决微表情识别中的数据不足和特征提取困难的问题。现有方法通常依赖于手工特征和关键帧，限制了其在复杂场景中的应用。

**核心思路**：论文提出了一种端到端的微动作感知深度学习框架，利用变换器和图卷积的优势，能够从原始视频帧中直接提取局部和全局特征，避免了对关键帧的依赖。

**技术框架**：整体架构包括F5C模块，该模块由全连接卷积和通道对应卷积组成，能够有效提取特征并建模特征模式之间的相关性。同时，MER、光流估计和面部关键点检测任务共享局部-全局特征进行联合训练。

**关键创新**：最重要的创新在于F5C模块的设计，结合了全连接卷积和图卷积，能够同时捕捉局部特征和全局上下文信息，这与传统方法的特征提取方式有本质区别。

**关键设计**：在网络结构上，采用了变换器风格的全连接卷积来提取局部特征，同时引入图风格的通道对应卷积来建模特征之间的关系。损失函数设计上，考虑了MER、光流估计和面部关键点检测的联合优化，以提升整体性能。

## 📊 实验亮点

实验结果表明，提出的框架在CASME II、SAMM和SMIC基准上均超越了现有最先进的MER方法，具体提升幅度达到XX%。此外，该框架在光流估计和面部关键点检测任务中也表现出色，验证了其在捕捉面部微小动作方面的有效性。

## 🎯 应用场景

该研究在微表情识别、情感分析和人机交互等领域具有广泛的应用潜力。通过提高微表情识别的准确性，可以在心理健康监测、社交机器人和虚拟现实等场景中实现更自然的交互体验。未来，该框架还可以扩展到其他视觉任务，如动作识别和行为分析。

## 📄 摘要（原文）

> Facial micro-expression recognition (MER) is a challenging problem, due to transient and subtle micro-expression (ME) actions. Most existing methods depend on hand-crafted features, key frames like onset, apex, and offset frames, or deep networks limited by small-scale and low-diversity datasets. In this paper, we propose an end-to-end micro-action-aware deep learning framework with advantages from transformer, graph convolution, and vanilla convolution. In particular, we propose a novel F5C block composed of fully-connected convolution and channel correspondence convolution to directly extract local-global features from a sequence of raw frames, without the prior knowledge of key frames. The transformer-style fully-connected convolution is proposed to extract local features while maintaining global receptive fields, and the graph-style channel correspondence convolution is introduced to model the correlations among feature patterns. Moreover, MER, optical flow estimation, and facial landmark detection are jointly trained by sharing the local-global features. The two latter tasks contribute to capturing facial subtle action information for MER, which can alleviate the impact of insufficient training data. Extensive experiments demonstrate that our framework (i) outperforms the state-of-the-art MER methods on CASME II, SAMM, and SMIC benchmarks, (ii) works well for optical flow estimation and facial landmark detection, and (iii) can capture facial subtle muscle actions in local regions associated with MEs. The code is available at https://github.com/CYF-cuber/MOL.

