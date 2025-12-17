---
layout: default
title: Data Selection for Fine-tuning Vision Language Models via Cross Modal Alignment Trajectories
---

# Data Selection for Fine-tuning Vision Language Models via Cross Modal Alignment Trajectories

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.01454" target="_blank" class="toolbar-btn">arXiv: 2510.01454v1</a>
    <a href="https://arxiv.org/pdf/2510.01454.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.01454v1" 
            onclick="toggleFavorite(this, '2510.01454v1', 'Data Selection for Fine-tuning Vision Language Models via Cross Modal Alignment Trajectories')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Nilay Naharas, Dang Nguyen, Nesihan Bulut, Mohammadhossein Bateni, Vahab Mirrokni, Baharan Mirzasoleiman

**分类**: cs.CV, cs.LG

**发布日期**: 2025-10-01

**备注**: 30 pages, 10 figures, 5 tables, link: https://bigml-cs-ucla.github.io/XMAS-project-page/

**🔗 代码/项目**: [PROJECT_PAGE](https://bigml-cs-ucla.github.io/XMAS-project-page/)

---

## 💡 一句话要点

**提出XMAS方法，通过跨模态对齐轨迹进行视觉语言模型高效数据选择。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉语言模型` `数据选择` `指令微调` `跨模态对齐` `注意力机制`

## 📋 核心要点

1. 现有LVLM数据选择方法效果不佳，无法有效去除训练数据中的冗余，甚至不如随机选择。
2. XMAS方法通过分析跨模态注意力矩阵的轨迹，识别并去除冗余样本，保留信息量大的样本。
3. 实验表明，XMAS能显著减少训练数据量，同时保持甚至提升模型在下游任务上的性能。

## 📝 摘要（中文）

本文旨在解决大规模视觉语言模型（LVLM）指令微调中的数据冗余问题。现有数据选择方法在不同子集大小下均无法超越随机选择。为此，本文提出了一种基于原则性的LVLM指令微调数据高效选择方法XMAS。该方法证明，指令微调期间具有相似跨模态注意力矩阵的样本具有相似的梯度，从而以类似的方式影响模型参数。XMAS通过对小型代理LVLM微调获得的注意力矩阵的顶部奇异值轨迹进行聚类，然后从中采样平衡子集，有效去除大规模LVLM训练数据中的冗余。实验表明，XMAS可以在完全保持LLaVA-1.5-7B在10个下游基准上的性能的同时，丢弃LLaVA-665k数据集的50%和Vision-Flan数据集的85%，并将其训练速度提高1.2倍。与LLaVA-665k的最佳基线相比，数据缩减幅度提高了30%。

## 🔬 方法详解

**问题定义**：论文旨在解决大规模视觉语言模型（LVLM）在指令微调过程中数据冗余的问题。现有数据选择方法，如基于梯度的方法或基于信息论的方法，在LVLM上表现不佳，无法有效去除冗余数据，甚至不如随机选择。这导致训练效率低下，浪费计算资源。

**核心思路**：论文的核心思路是，具有相似跨模态注意力矩阵的样本，在指令微调过程中对模型参数的影响相似，因此可以被认为是冗余的。通过识别和去除这些冗余样本，可以减少训练数据量，提高训练效率，同时保持模型性能。

**技术框架**：XMAS方法的整体框架包括以下几个阶段：1. 使用小型代理LVLM进行初步微调。2. 提取训练样本在微调过程中的跨模态注意力矩阵。3. 对每个样本的注意力矩阵计算顶部奇异值，并记录其随训练步数变化的轨迹。4. 基于奇异值轨迹对样本进行聚类。5. 从每个聚类中采样代表性样本，组成最终的训练子集。

**关键创新**：XMAS的关键创新在于利用跨模态注意力矩阵的轨迹来衡量样本之间的相似性。与直接比较注意力矩阵或梯度相比，注意力矩阵轨迹能够捕捉样本在训练过程中的动态变化，更准确地反映样本对模型参数的影响。此外，通过奇异值分解，可以提取注意力矩阵的主要特征，降低计算复杂度。

**关键设计**：XMAS的关键设计包括：1. 使用小型代理LVLM加速注意力矩阵的提取。2. 选择顶部奇异值作为注意力矩阵的代表性特征。3. 使用K-means等聚类算法对奇异值轨迹进行聚类。4. 在每个聚类中，根据样本与聚类中心的距离，选择代表性样本。论文还采用了平衡采样策略，确保每个聚类都有样本被选中。

## 📊 实验亮点

实验结果表明，XMAS方法在LLaVA-665k数据集上可以丢弃50%的数据，在Vision-Flan数据集上可以丢弃85%的数据，同时完全保持LLaVA-1.5-7B模型在10个下游基准上的性能。此外，XMAS方法还可以将训练速度提高1.2倍，并且比LLaVA-665k的最佳基线的数据缩减幅度提高了30%。

## 🎯 应用场景

XMAS方法可广泛应用于各种视觉语言模型的指令微调场景，尤其是在数据量庞大、计算资源有限的情况下。该方法能够有效降低训练成本，加速模型迭代，并提升模型在下游任务上的泛化能力。此外，该方法还可以用于构建更高效的数据集，促进视觉语言模型的研究和应用。

## 📄 摘要（原文）

> Data-efficient learning aims to eliminate redundancy in large training datasets by training models on smaller subsets of the most informative examples. While data selection has been extensively explored for vision models and large language models (LLMs), it remains underexplored for Large Vision-Language Models (LVLMs). Notably, none of existing methods can outperform random selection at different subset sizes. In this work, we propose the first principled method for data-efficient instruction tuning of LVLMs. We prove that examples with similar cross-modal attention matrices during instruction tuning have similar gradients. Thus, they influence model parameters in a similar manner and convey the same information to the model during training. Building on this insight, we propose XMAS, which clusters examples based on the trajectories of the top singular values of their attention matrices obtained from fine-tuning a small proxy LVLM. By sampling a balanced subset from these clusters, XMAS effectively removes redundancy in large-scale LVLM training data. Extensive experiments show that XMAS can discard 50% of the LLaVA-665k dataset and 85% of the Vision-Flan dataset while fully preserving performance of LLaVA-1.5-7B on 10 downstream benchmarks and speeding up its training by 1.2x. This is 30% more data reduction compared to the best baseline for LLaVA-665k. The project's website can be found at https://bigml-cs-ucla.github.io/XMAS-project-page/.

