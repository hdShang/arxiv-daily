---
layout: default
title: "ReconMOST: Multi-Layer Sea Temperature Reconstruction with Observations-Guided Diffusion"
---

# ReconMOST: Multi-Layer Sea Temperature Reconstruction with Observations-Guided Diffusion

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.10391" class="toolbar-btn" target="_blank">📄 arXiv: 2506.10391v1</a>
  <a href="https://arxiv.org/pdf/2506.10391.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.10391v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.10391v1', 'ReconMOST: Multi-Layer Sea Temperature Reconstruction with Observations-Guided Diffusion')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuanyi Song, Pumeng Lyu, Ben Fei, Fenghua Ling, Wanli Ouyang, Lei Bai

**分类**: cs.CV

**发布日期**: 2025-06-12

**🔗 代码/项目**: [GITHUB](https://github.com/norsheep/ReconMOST)

---

## 💡 一句话要点

**提出ReconMOST以解决海洋温度重建问题**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)**

**关键词**: `海洋温度重建` `引导扩散模型` `机器学习` `气候动态` `数据稀疏`

## 📋 核心要点

1. 传统海洋温度重建方法面临数据稀疏、算法复杂和计算成本高等挑战，影响了重建精度和效率。
2. 本文提出ReconMOST，通过预训练扩散模型和引导反向扩散过程，实现多层海温的高效重建，克服了现有方法的局限性。
3. 实验结果显示，ReconMOST在重建精度上表现优异，均方误差（MSE）值分别为0.049（引导）、0.680（重建）和0.633（总），验证了其有效性。

## 📝 摘要（中文）

准确重建海洋温度对于反映全球气候动态和支持海洋气象研究至关重要。传统方法因数据稀疏、算法复杂性和高计算成本面临挑战，而机器学习方法在海面和局部区域的重建中应用有限，尤其在云遮挡等问题上表现不佳。为了解决这些局限性，本文提出了ReconMOST，一个基于数据驱动的引导扩散模型框架，用于多层海温重建。通过预训练无条件扩散模型，利用历史数值模拟数据，使模型获得物理一致的海洋温度场分布模式。在生成阶段，利用稀疏但高精度的现场观测数据作为反向扩散过程的引导点，生成准确的重建结果。我们的模型在CMIP6数值模拟数据上进行预训练，并在CMIP6和EN4分析数据上进行引导重建实验，结果表明该框架的有效性和鲁棒性。

## 🔬 方法详解

**问题定义**：本文旨在解决海洋温度重建中的数据稀疏和算法复杂性问题。现有方法在处理缺乏观测数据的区域时，重建结果往往不够准确，影响了气候研究的可靠性。

**核心思路**：本文提出的ReconMOST框架通过预训练无条件扩散模型，利用历史数值模拟数据学习海洋温度的物理一致性分布，并在生成阶段结合高精度现场观测数据进行引导，确保重建结果的准确性。

**技术框架**：ReconMOST的整体架构包括两个主要阶段：预训练阶段和生成阶段。在预训练阶段，模型通过大量历史数据学习温度场的分布模式；在生成阶段，利用稀疏的观测数据作为引导点，进行反向扩散生成重建结果。

**关键创新**：该研究的核心创新在于将引导扩散模型应用于多层海温重建，突破了传统方法在数据稀疏情况下的局限，能够在缺乏直接观测数据的区域实现物理一致的重建。

**关键设计**：模型的关键设计包括选择合适的损失函数以平衡重建精度和物理一致性，以及优化网络结构以提高模型的泛化能力。

## 📊 实验亮点

实验结果表明，ReconMOST在重建精度上表现优异，均方误差（MSE）值分别为0.049（引导）、0.680（重建）和0.633（总），在处理92.5%的缺失数据时，仍能保持较高的重建准确性和空间分辨率，展示了其卓越的鲁棒性和泛化能力。

## 🎯 应用场景

该研究的ReconMOST框架具有广泛的应用潜力，能够为全球海洋温度监测、气候变化研究及海洋气象预报提供重要支持。其高效的重建能力将推动海洋科学研究的深入发展，尤其是在数据稀缺的区域。

## 📄 摘要（原文）

> Accurate reconstruction of ocean is essential for reflecting global climate dynamics and supporting marine meteorological research. Conventional methods face challenges due to sparse data, algorithmic complexity, and high computational costs, while increasing usage of machine learning (ML) method remains limited to reconstruction problems at the sea surface and local regions, struggling with issues like cloud occlusion. To address these limitations, this paper proposes ReconMOST, a data-driven guided diffusion model framework for multi-layer sea temperature reconstruction. Specifically, we first pre-train an unconditional diffusion model using a large collection of historical numerical simulation data, enabling the model to attain physically consistent distribution patterns of ocean temperature fields. During the generation phase, sparse yet high-accuracy in-situ observational data are utilized as guidance points for the reverse diffusion process, generating accurate reconstruction results. Importantly, in regions lacking direct observational data, the physically consistent spatial distribution patterns learned during pre-training enable implicitly guided and physically plausible reconstructions. Our method extends ML-based SST reconstruction to a global, multi-layer setting, handling over 92.5% missing data while maintaining reconstruction accuracy, spatial resolution, and superior generalization capability. We pre-train our model on CMIP6 numerical simulation data and conduct guided reconstruction experiments on CMIP6 and EN4 analysis data. The results of mean squared error (MSE) values achieve 0.049 on guidance, 0.680 on reconstruction, and 0.633 on total, respectively, demonstrating the effectiveness and robustness of the proposed framework. Our source code is available at https://github.com/norsheep/ReconMOST.

