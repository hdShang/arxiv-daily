---
layout: default
title: Learning Heterogeneous Mixture of Scene Experts for Large-scale Neural Radiance Fields
---

# Learning Heterogeneous Mixture of Scene Experts for Large-scale Neural Radiance Fields

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.02005" class="toolbar-btn" target="_blank">📄 arXiv: 2505.02005v2</a>
  <a href="https://arxiv.org/pdf/2505.02005.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.02005v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.02005v2', 'Learning Heterogeneous Mixture of Scene Experts for Large-scale Neural Radiance Fields')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhenxing Mi, Ping Yin, Xue Xiao, Dan Xu

**分类**: cs.CV

**发布日期**: 2025-05-04 (更新: 2025-08-25)

**备注**: Accepted by TPAMI

**🔗 代码/项目**: [GITHUB](https://github.com/MiZhenxing/Switch-NeRF)

---

## 💡 一句话要点

**提出Switch-NeRF++以解决大规模场景建模的异质性与效率问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `大规模场景建模` `神经辐射场` `异质混合专家` `场景分解` `高效渲染` `深度学习` `计算机视觉`

## 📋 核心要点

1. 现有NeRF方法在大规模场景建模中面临可学习分解、场景异质性建模和效率等关键问题。
2. 本文提出Switch-NeRF++，通过门控网络实现场景分解，并将3D点分配给专门的NeRF专家，提升建模效率。
3. 实验结果显示，该方法在大规模场景渲染中实现了8倍的训练加速和16倍的渲染加速，达到最先进的渲染精度。

## 📝 摘要（中文）

近年来，针对大规模场景的NeRF方法强调了场景分解在可扩展NeRF中的重要性。尽管已有方法在可扩展性上取得了一定进展，但仍存在可学习分解、场景异质性建模和建模效率等关键问题未被充分探索。本文提出了Switch-NeRF++，一种异质混合哈希专家网络（HMoHE），在统一框架内解决这些挑战。该框架通过门控网络学习场景分解，并将3D点分配给专门的NeRF专家，采用稀疏门控混合专家（MoE）NeRF框架进行共同优化。通过哈希网络和不同分辨率范围的异质哈希专家，Switch-NeRF++实现了对大规模场景的高效学习。实验结果表明，该方法在现有大规模NeRF数据集和UrbanBIS的新数据集上表现出色，训练速度提升8倍，渲染速度提升16倍。

## 🔬 方法详解

**问题定义**：本文旨在解决大规模场景建模中的异质性与效率问题，现有方法在场景分解和建模效率方面存在不足。

**核心思路**：Switch-NeRF++通过引入门控网络和异质哈希专家，实现对场景的高效分解与建模，采用稀疏门控混合专家框架共同优化。

**技术框架**：整体架构包括门控网络和多个异质哈希专家，门控网络负责场景分解，哈希专家则根据不同分辨率处理3D点，形成高效的学习流程。

**关键创新**：该方法的核心创新在于引入了哈希网络和异质专家的组合，使得对大规模场景的建模更加灵活和高效，与传统方法相比，显著提升了处理能力。

**关键设计**：在设计中，采用了不同分辨率的哈希网格，优化了门控网络的学习过程，确保了模型在处理大规模场景时的高效性和准确性。通过稀疏门控机制，进一步提升了模型的训练和渲染速度。

## 📊 实验亮点

实验结果表明，Switch-NeRF++在大规模场景渲染中实现了8倍的训练加速和16倍的渲染加速，相较于Switch-NeRF，显著提升了渲染精度，展示了其在大规模场景建模中的优越性能。

## 🎯 应用场景

该研究具有广泛的应用潜力，尤其在城市建模、虚拟现实和游戏开发等领域。通过高效的场景建模能力，Switch-NeRF++能够为实时渲染和交互式应用提供支持，推动相关技术的发展与应用。

## 📄 摘要（原文）

> Recent NeRF methods on large-scale scenes have underlined the importance of scene decomposition for scalable NeRFs. Although achieving reasonable scalability, there are several critical problems remaining unexplored, i.e., learnable decomposition, modeling scene heterogeneity, and modeling efficiency. In this paper, we introduce Switch-NeRF++, a Heterogeneous Mixture of Hash Experts (HMoHE) network that addresses these challenges within a unified framework. It is a highly scalable NeRF that learns heterogeneous decomposition and heterogeneous NeRFs efficiently for large-scale scenes in an end-to-end manner. In our framework, a gating network learns to decompose scenes and allocates 3D points to specialized NeRF experts. This gating network is co-optimized with the experts by our proposed Sparsely Gated Mixture of Experts (MoE) NeRF framework. We incorporate a hash-based gating network and distinct heterogeneous hash experts. The hash-based gating efficiently learns the decomposition of the large-scale scene. The distinct heterogeneous hash experts consist of hash grids of different resolution ranges, enabling effective learning of the heterogeneous representation of different scene parts. These design choices make our framework an end-to-end and highly scalable NeRF solution for real-world large-scale scene modeling to achieve both quality and efficiency. We evaluate our accuracy and scalability on existing large-scale NeRF datasets and a new dataset with very large-scale scenes ($>6.5km^2$) from UrbanBIS. Extensive experiments demonstrate that our approach can be easily scaled to various large-scale scenes and achieve state-of-the-art scene rendering accuracy. Furthermore, our method exhibits significant efficiency, with an 8x acceleration in training and a 16x acceleration in rendering compared to Switch-NeRF. Codes will be released at https://github.com/MiZhenxing/Switch-NeRF.

