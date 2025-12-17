---
layout: default
title: BalanceGS: Algorithm-System Co-design for Efficient 3D Gaussian Splatting Training on GPU
---

# BalanceGS: Algorithm-System Co-design for Efficient 3D Gaussian Splatting Training on GPU

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.14564" target="_blank" class="toolbar-btn">arXiv: 2510.14564v1</a>
    <a href="https://arxiv.org/pdf/2510.14564.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.14564v1" 
            onclick="toggleFavorite(this, '2510.14564v1', 'BalanceGS: Algorithm-System Co-design for Efficient 3D Gaussian Splatting Training on GPU')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Junyi Wu, Jiaming Xu, Jinhao Li, Yongkang Zhou, Jiayi Pan, Xingyang Li, Guohao Dai

**分类**: cs.CV

**发布日期**: 2025-10-16

**备注**: Accepted by ASP-DAC 2026

---

## 💡 一句话要点

**BalanceGS：面向GPU的3D高斯溅射高效训练的算法-系统协同设计**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `3D高斯溅射` `三维重建` `算法系统协同设计` `GPU加速` `负载均衡`

## 📋 核心要点

1. 传统3DGS训练在高斯致密化、投影和颜色溅射阶段存在密度分配倾斜、计算负载不均和内存访问碎片化等问题。
2. BalanceGS通过算法和系统协同设计，包括启发式密度控制、相似性采样合并和重排序内存访问，解决上述效率瓶颈。
3. 实验表明，BalanceGS在NVIDIA A100 GPU上实现了1.44倍的训练加速，同时保持了可比的重建质量。

## 📝 摘要（中文）

3D高斯溅射(3DGS)已成为一种有前景的3D重建技术。传统的3DGS训练流程包括三个连续的步骤：高斯致密化、高斯投影和颜色溅射。尽管其重建质量很有前景，但这种传统方法存在三个关键的效率低下问题：(1)高斯致密化期间的密度分配倾斜，(2)高斯投影期间的计算工作负载不平衡，以及(3)颜色溅射期间的内存访问碎片化。为了解决上述挑战，我们提出了BalanceGS，这是一种用于3DGS高效训练的算法-系统协同设计。(1)在算法层面，我们提出了启发式的工作负载敏感的高斯密度控制，以自动平衡点分布——消除密集区域中80%的冗余高斯，同时填补稀疏区域的空白。(2)在系统层面，我们提出了基于相似性的高斯采样和合并，它用自适应工作负载分配取代了静态的一对一线程-像素映射——线程现在根据局部集群密度动态处理可变数量的高斯。(3)在映射层面，我们提出了一种基于重排序的内存访问映射策略，该策略重构了RGB存储，并支持在共享内存中进行批量加载。大量的实验表明，与3DGS相比，我们的方法在NVIDIA A100 GPU上实现了1.44倍的训练加速，而质量下降可以忽略不计。

## 🔬 方法详解

**问题定义**：论文旨在解决3D高斯溅射（3DGS）训练过程中存在的效率瓶颈。具体来说，现有方法在高斯致密化阶段存在密度分配不均，导致部分区域高斯过多冗余，而部分区域高斯不足；在高斯投影阶段，计算负载在不同线程间不平衡；在颜色溅射阶段，内存访问模式零散，效率低下。这些问题严重影响了3DGS的训练速度和资源利用率。

**核心思路**：BalanceGS的核心思路是通过算法和系统协同设计，实现3DGS训练过程中的负载均衡和内存访问优化。算法层面，通过启发式密度控制平衡高斯分布；系统层面，通过相似性采样合并实现自适应工作负载分配，并通过重排序优化内存访问。这种协同设计旨在充分利用GPU的并行计算能力，提高训练效率。

**技术框架**：BalanceGS的整体框架包含三个主要部分：1) 启发式工作负载敏感的高斯密度控制：根据局部密度动态调整高斯数量，减少冗余并填补空白。2) 基于相似性的高斯采样和合并：将静态线程-像素映射改为动态分配，线程根据局部密度处理不同数量的高斯。3) 基于重排序的内存访问映射：重组RGB数据存储，实现批量加载到共享内存，减少内存访问延迟。

**关键创新**：BalanceGS的关键创新在于算法和系统的协同优化。传统的3DGS训练流程各个阶段相互独立，优化空间有限。BalanceGS打破了这种割裂，通过算法层面的密度控制为系统层面的负载均衡创造条件，并通过系统层面的优化反过来提升算法的效率。这种协同设计是BalanceGS能够取得显著性能提升的关键。

**关键设计**：启发式密度控制采用了一种基于工作负载敏感的策略，根据局部高斯密度动态调整高斯数量。相似性采样和合并算法基于高斯特征的相似度进行聚类，将相似的高斯分配给同一线程处理。重排序内存访问映射通过重新排列RGB数据，使得相邻像素的数据在内存中也相邻，从而实现批量加载。

## 📊 实验亮点

实验结果表明，BalanceGS在NVIDIA A100 GPU上实现了1.44倍的训练加速，同时保持了与原始3DGS相当的重建质量。通过消除80%的冗余高斯，BalanceGS显著降低了计算负担。这些结果验证了BalanceGS在提高3DGS训练效率方面的有效性。

## 🎯 应用场景

BalanceGS的潜在应用领域包括三维重建、虚拟现实、增强现实、自动驾驶等。通过提高3DGS的训练效率，BalanceGS可以加速这些领域中三维模型的生成和优化，降低计算成本，并促进更广泛的应用。未来，BalanceGS的思路可以推广到其他基于点云的渲染和重建方法中。

## 📄 摘要（原文）

> 3D Gaussian Splatting (3DGS) has emerged as a promising 3D reconstruction technique. The traditional 3DGS training pipeline follows three sequential steps: Gaussian densification, Gaussian projection, and color splatting. Despite its promising reconstruction quality, this conventional approach suffers from three critical inefficiencies: (1) Skewed density allocation during Gaussian densification, (2) Imbalanced computation workload during Gaussian projection and (3) Fragmented memory access during color splatting.
>   To tackle the above challenges, we introduce BalanceGS, the algorithm-system co-design for efficient training in 3DGS. (1) At the algorithm level, we propose heuristic workload-sensitive Gaussian density control to automatically balance point distributions - removing 80% redundant Gaussians in dense regions while filling gaps in sparse areas. (2) At the system level, we propose Similarity-based Gaussian sampling and merging, which replaces the static one-to-one thread-pixel mapping with adaptive workload distribution - threads now dynamically process variable numbers of Gaussians based on local cluster density. (3) At the mapping level, we propose reordering-based memory access mapping strategy that restructures RGB storage and enables batch loading in shared memory.
>   Extensive experiments demonstrate that compared with 3DGS, our approach achieves a 1.44$\times$ training speedup on a NVIDIA A100 GPU with negligible quality degradation.

