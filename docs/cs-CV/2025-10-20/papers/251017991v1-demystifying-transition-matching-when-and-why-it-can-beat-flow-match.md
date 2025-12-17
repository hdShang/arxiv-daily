---
layout: default
title: Demystifying Transition Matching: When and Why It Can Beat Flow Matching
---

# Demystifying Transition Matching: When and Why It Can Beat Flow Matching

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.17991" class="toolbar-btn" target="_blank">📄 arXiv: 2510.17991v1</a>
  <a href="https://arxiv.org/pdf/2510.17991.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.17991v1" onclick="toggleFavorite(this, '2510.17991v1', 'Demystifying Transition Matching: When and Why It Can Beat Flow Matching')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jaihoon Kim, Rajarshi Saha, Minhyuk Sung, Youngsuk Park

**分类**: cs.LG, cs.CV

**发布日期**: 2025-10-20

---

## 💡 一句话要点

**揭示Transition Matching优势：在高斯分布及混合模型中超越Flow Matching**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `生成模型` `Flow Matching` `Transition Matching` `高斯分布` `高斯混合模型`

## 📋 核心要点

1. Flow Matching (FM)作为先进生成模型的基础，存在采样效率的挑战，Transition Matching (TM)在特定情况下表现更优。
2. 论文核心在于分析TM优于FM的条件，特别是在目标分布为高斯分布或高斯混合模型时，TM如何通过随机更新和模式分离实现更优性能。
3. 实验验证了理论分析，表明在具有良好分离模式和非零方差的目标分布上，TM在图像和视频生成等实际应用中表现更佳。

## 📝 摘要（中文）

Flow Matching (FM) 是许多先进生成模型的基础，但最近的结果表明，Transition Matching (TM) 可以用更少的采样步骤实现更高的质量。本文旨在解答 TM 何时以及为何优于 FM 的问题。首先，当目标是单峰高斯分布时，我们证明对于有限数量的步骤，TM 实现了比 FM 严格更低的 KL 散度。这种改进源于 TM 中随机差分潜在更新，它保留了确定性 FM 低估的目标协方差。然后，我们描述了收敛速度，表明在固定的计算预算下，TM 比 FM 实现更快的收敛速度，从而确立了其在单峰高斯环境中的优势。其次，我们将分析扩展到高斯混合模型，并确定局部单峰状态，其中采样动态近似于单峰情况，TM 可以优于 FM。当分量均值之间的最小距离增加时，近似误差减小，突出了 TM 在模式分离良好的情况下更受欢迎。但是，当目标方差接近零时，每个 TM 更新都会收敛到 FM 更新，并且 TM 的性能优势会减小。总而言之，我们表明，当目标分布具有良好分离的模式和非零方差时，TM 优于 FM。我们通过对高斯分布的受控实验验证了我们的理论结果，并将比较扩展到图像和视频生成的实际应用。

## 🔬 方法详解

**问题定义**：论文旨在解决在生成模型中，Flow Matching (FM) 方法在特定情况下采样效率不高的问题。现有FM方法在处理具有良好分离模式和非零方差的目标分布时，可能存在收敛速度慢，以及对目标分布的协方差估计不足的问题。

**核心思路**：论文的核心思路是分析Transition Matching (TM) 方法在特定条件下的优势。TM通过引入随机差分潜在更新，能够更好地保留目标分布的协方差，从而在目标分布具有良好分离的模式和非零方差时，实现比FM更快的收敛速度和更高的生成质量。

**技术框架**：论文的技术框架主要包括以下几个部分：1) 对单峰高斯分布下TM和FM的KL散度进行理论分析，证明TM具有更低的KL散度。2) 推导TM和FM的收敛速度，表明在固定计算预算下，TM收敛更快。3) 将分析扩展到高斯混合模型，确定TM优于FM的局部单峰状态。4) 通过实验验证理论分析，并在图像和视频生成等实际应用中比较TM和FM的性能。

**关键创新**：论文最重要的技术创新点在于揭示了TM优于FM的条件，即当目标分布具有良好分离的模式和非零方差时，TM通过随机差分潜在更新能够更好地保留目标分布的协方差，从而实现更优的性能。与FM的确定性更新相比，TM的随机性是其优势的关键。

**关键设计**：论文的关键设计包括：1) 使用KL散度作为评估生成模型性能的指标。2) 通过理论分析推导TM和FM的收敛速度。3) 在高斯混合模型中，引入模式分离程度作为影响TM和FM性能的关键因素。4) 通过控制实验验证理论分析，并在图像和视频生成等实际应用中比较TM和FM的性能。

## 📊 实验亮点

实验结果表明，在单峰高斯分布下，TM比FM具有更低的KL散度和更快的收敛速度。在高斯混合模型中，当模式分离良好且方差非零时，TM显著优于FM。在图像和视频生成任务中，TM也表现出更好的性能，尤其是在生成具有多个清晰模式的数据时。

## 🎯 应用场景

该研究成果可应用于图像生成、视频生成等领域，尤其是在需要生成具有多个清晰可辨识模式的数据时，例如生成具有不同风格的人脸图像或包含多个独立运动对象的视频。通过使用Transition Matching，可以提高生成模型的采样效率和生成质量，从而降低计算成本并提升用户体验。未来的研究可以探索如何将Transition Matching应用于更复杂的生成任务和更大规模的数据集。

## 📄 摘要（原文）

> Flow Matching (FM) underpins many state-of-the-art generative models, yet recent results indicate that Transition Matching (TM) can achieve higher quality with fewer sampling steps. This work answers the question of when and why TM outperforms FM. First, when the target is a unimodal Gaussian distribution, we prove that TM attains strictly lower KL divergence than FM for finite number of steps. The improvement arises from stochastic difference latent updates in TM, which preserve target covariance that deterministic FM underestimates. We then characterize convergence rates, showing that TM achieves faster convergence than FM under a fixed compute budget, establishing its advantage in the unimodal Gaussian setting. Second, we extend the analysis to Gaussian mixtures and identify local-unimodality regimes in which the sampling dynamics approximate the unimodal case, where TM can outperform FM. The approximation error decreases as the minimal distance between component means increases, highlighting that TM is favored when the modes are well separated. However, when the target variance approaches zero, each TM update converges to the FM update, and the performance advantage of TM diminishes. In summary, we show that TM outperforms FM when the target distribution has well-separated modes and non-negligible variances. We validate our theoretical results with controlled experiments on Gaussian distributions, and extend the comparison to real-world applications in image and video generation.

