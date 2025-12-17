---
layout: default
title: CrossRay3D: Geometry and Distribution Guidance for Efficient Multimodal 3D Detection
---

# CrossRay3D: Geometry and Distribution Guidance for Efficient Multimodal 3D Detection

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.15991" target="_blank" class="toolbar-btn">arXiv: 2510.15991v3</a>
    <a href="https://arxiv.org/pdf/2510.15991.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.15991v3" 
            onclick="toggleFavorite(this, '2510.15991v3', 'CrossRay3D: Geometry and Distribution Guidance for Efficient Multimodal 3D Detection')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Huiming Yang, Wenzhuo Liu, Yicheng Qiao, Lei Yang, Xianzhu Zeng, Li Wang, Zhiwei Li, Zijian Zeng, Zhiying Jiang, Huaping Liu, Kunfeng Wang

**分类**: cs.CV

**发布日期**: 2025-10-14 (更新: 2025-11-04)

**备注**: 13 pages

---

## 💡 一句话要点

**CrossRay3D：通过几何与分布引导提升多模态3D检测效率**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态3D检测` `稀疏检测器` `几何信息` `类别平衡` `自动驾驶`

## 📋 核心要点

1. 现有稀疏多模态3D检测器忽略了token表征的质量，导致前景质量不佳，限制了检测性能。
2. CrossRay3D通过引入Ray-Aware Supervision和Class-Balanced Supervision，增强token的几何信息和类别语义表征。
3. 实验表明，CrossRay3D在nuScenes数据集上取得了SOTA性能，并在数据缺失情况下表现出良好的鲁棒性。

## 📝 摘要（中文）

本文提出了一种名为CrossRay3D的高效多模态3D检测器。针对现有稀疏检测器token表征质量不高，导致前景质量欠佳和性能受限的问题，本文提出Sparse Selector (SS)。SS的核心模块是Ray-Aware Supervision (RAS)，它在训练阶段保留丰富的几何信息，以及Class-Balanced Supervision，自适应地重新加权类别语义的重要性，确保与小物体相关的token在token采样期间被保留，从而优于其他稀疏多模态检测器。此外，本文设计了Ray Positional Encoding (Ray PE)来解决LiDAR模态和图像之间的分布差异。在nuScenes基准测试中，CrossRay3D实现了72.4 mAP和74.7 NDS的state-of-the-art性能，并且比其他领先方法快1.84倍。CrossRay3D在LiDAR或相机数据部分或完全缺失的情况下也表现出强大的鲁棒性。

## 🔬 方法详解

**问题定义**：现有稀疏多模态3D检测器在token表征质量上存在不足，导致检测精度受限，尤其是在小物体检测方面表现不佳。这些检测器通常无法充分利用几何结构信息和类别分布信息，从而影响了整体性能。

**核心思路**：本文的核心思路是通过引入几何结构和类别分布的引导，来提升token表征的质量。具体来说，通过Ray-Aware Supervision保留丰富的几何信息，并通过Class-Balanced Supervision自适应地调整类别语义的重要性，从而改善token的采样和选择过程。这样设计的目的是使检测器能够更好地关注前景目标，特别是小物体。

**技术框架**：CrossRay3D是一个端到端的稀疏多模态3D检测器，其主要组成部分包括：1) 特征提取模块（用于提取LiDAR和图像的特征）；2) Sparse Selector (SS)模块，包含Ray-Aware Supervision (RAS)和Class-Balanced Supervision；3) Ray Positional Encoding (Ray PE)模块；4) 检测头。整体流程是首先提取多模态特征，然后通过SS模块选择高质量的token，并利用Ray PE模块进行位置编码，最后通过检测头进行3D目标检测。

**关键创新**：本文最重要的技术创新点在于Sparse Selector (SS)模块，特别是其中的Ray-Aware Supervision (RAS)和Class-Balanced Supervision。RAS通过射线感知的监督方式，在训练阶段保留丰富的几何信息，这与传统的监督方式不同，后者可能忽略了重要的几何结构。Class-Balanced Supervision则通过自适应地调整类别权重，解决了小物体检测中的类别不平衡问题。

**关键设计**：Ray-Aware Supervision (RAS)的具体实现方式是，在训练过程中，对每个token引入射线方向的监督信号，鼓励网络学习token与射线之间的几何关系。Class-Balanced Supervision的具体实现方式是，根据每个类别的样本数量，动态地调整损失函数的权重，使得小样本类别能够获得更大的关注。Ray Positional Encoding (Ray PE)的设计考虑了LiDAR和图像在空间分布上的差异，通过引入射线方向的位置编码，使得网络能够更好地理解多模态特征之间的关系。

## 📊 实验亮点

CrossRay3D在nuScenes数据集上取得了显著的性能提升，mAP达到72.4，NDS达到74.7，超越了现有的SOTA方法。更重要的是，CrossRay3D在保持高性能的同时，实现了1.84倍的加速，使其在实际应用中更具优势。此外，该方法在LiDAR或相机数据部分或完全缺失的情况下，仍然表现出强大的鲁棒性，证明了其在恶劣环境下的可靠性。

## 🎯 应用场景

CrossRay3D具有广泛的应用前景，包括自动驾驶、机器人导航、智能交通等领域。其高效的计算性能和强大的鲁棒性使其能够在资源受限的平台上部署，并适应各种复杂的环境条件。该研究的未来影响在于推动多模态3D感知技术的发展，并为更安全、更智能的自主系统提供技术支持。

## 📄 摘要（原文）

> The sparse cross-modality detector offers more advantages than its counterpart, the Bird's-Eye-View (BEV) detector, particularly in terms of adaptability for downstream tasks and computational cost savings. However, existing sparse detectors overlook the quality of token representation, leaving it with a sub-optimal foreground quality and limited performance. In this paper, we identify that the geometric structure preserved and the class distribution are the key to improving the performance of the sparse detector, and propose a Sparse Selector (SS). The core module of SS is Ray-Aware Supervision (RAS), which preserves rich geometric information during the training stage, and Class-Balanced Supervision, which adaptively reweights the salience of class semantics, ensuring that tokens associated with small objects are retained during token sampling. Thereby, outperforming other sparse multi-modal detectors in the representation of tokens. Additionally, we design Ray Positional Encoding (Ray PE) to address the distribution differences between the LiDAR modality and the image. Finally, we integrate the aforementioned module into an end-to-end sparse multi-modality detector, dubbed CrossRay3D. Experiments show that, on the challenging nuScenes benchmark, CrossRay3D achieves state-of-the-art performance with 72.4 mAP and 74.7 NDS, while running 1.84 faster than other leading methods. Moreover, CrossRay3D demonstrates strong robustness even in scenarios where LiDAR or camera data are partially or entirely missing.

