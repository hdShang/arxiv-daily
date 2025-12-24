---
layout: default
title: "AtmosMJ: Revisiting Gating Mechanism for AI Weather Forecasting Beyond the Year Scale"
---

# AtmosMJ: Revisiting Gating Mechanism for AI Weather Forecasting Beyond the Year Scale

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.09733" class="toolbar-btn" target="_blank">📄 arXiv: 2506.09733v3</a>
  <a href="https://arxiv.org/pdf/2506.09733.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.09733v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.09733v3', 'AtmosMJ: Revisiting Gating Mechanism for AI Weather Forecasting Beyond the Year Scale')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Minjong Cheon

**分类**: cs.LG, cs.AI, cs.CV, physics.ao-ph

**发布日期**: 2025-06-11 (更新: 2025-08-18)

**备注**: All authors of this manuscript have not reached a consensus on its submission to arXiv. Since at least one co-author does not agree with the current version being publicly available, we respectfully request the withdrawal of this preprint in accordance with the authors' collective decision

---

## 💡 一句话要点

**提出AtmosMJ以解决长时间天气预测的稳定性问题**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)**

**关键词**: `天气预测` `深度学习` `卷积网络` `长时间预测` `门控机制` `ERA5数据` `气象模型` `数据驱动`

## 📋 核心要点

1. 现有的天气预测模型在长时间范围内的稳定性仍然面临重大挑战，尤其是在超过几周的自回归预测中。
2. AtmosMJ通过直接在标准经纬度网格上操作ERA5数据，提出了一种新颖的门控残差融合机制，旨在提高长时间预测的稳定性。
3. 实验结果显示，AtmosMJ在500天的预测中表现出稳定性，并在10天的预测准确性上与Pangu-Weather和GraphCast等模型相当。

## 📝 摘要（中文）

大型天气模型（LWM）的出现标志着数据驱动预测的转折点，许多模型在中期范围内超越了传统数值系统。然而，实现超过几周的稳定长时间自回归预测仍然是一个重大挑战。现有的最先进模型，如SFNO和DLWP-HPX，依赖于将输入数据转换为非标准空间域，如球谐或HEALPix网格。这导致了普遍假设，即这种表示是强制物理一致性和长期稳定性所必需的。本文挑战了这一假设，研究在标准的经纬度网格上是否可以实现可比的长期性能。我们提出了AtmosMJ，一个直接在ERA5数据上操作的深度卷积网络，无需任何球形重映射。模型的稳定性通过一种新颖的门控残差融合（GRF）机制得以实现，该机制自适应地调节特征更新，以防止在长时间递归模拟中错误累积。我们的结果表明，AtmosMJ能够产生约500天的稳定且物理上合理的预测。

## 🔬 方法详解

**问题定义**：本文旨在解决现有天气预测模型在长时间范围内的稳定性不足问题，尤其是那些依赖于非标准空间域的模型。

**核心思路**：AtmosMJ通过在标准经纬度网格上直接处理ERA5数据，避免了复杂的球形重映射，提出了一种新颖的门控残差融合机制，以调节特征更新，防止错误累积。

**技术框架**：AtmosMJ的整体架构包括数据输入模块、深度卷积网络和门控残差融合机制。模型通过ERA5数据进行训练，采用标准的经纬度网格进行预测。

**关键创新**：AtmosMJ的关键创新在于其门控残差融合机制，该机制允许模型在长时间预测中保持稳定性，与依赖于非标准数据表示的现有方法本质上不同。

**关键设计**：模型在设计上采用了低训练预算的策略，仅需5.7天的V100 GPU训练时间，且在损失函数和网络结构上进行了优化，以提高预测的准确性和稳定性。

## 📊 实验亮点

AtmosMJ在500天的预测中表现出稳定性，并在10天的预测准确性上与Pangu-Weather和GraphCast等模型相当，显示出其在长时间天气预测中的竞争力。模型训练仅需5.7天的V100 GPU时间，展现了高效的计算性能。

## 🎯 应用场景

AtmosMJ的研究成果可广泛应用于气象预报、气候变化研究和农业气象服务等领域。其高效的长时间天气预测能力将为决策支持系统提供更可靠的数据基础，具有重要的实际价值和潜在影响。

## 📄 摘要（原文）

> The advent of Large Weather Models (LWMs) has marked a turning point in data-driven forecasting, with many models now outperforming traditional numerical systems in the medium range. However, achieving stable, long-range autoregressive forecasts beyond a few weeks remains a significant challenge. Prevailing state-of-the-art models that achieve year-long stability, such as SFNO and DLWP-HPX, have relied on transforming input data onto non-standard spatial domains like spherical harmonics or HEALPix meshes. This has led to the prevailing assumption that such representations are necessary to enforce physical consistency and long-term stability. This paper challenges that assumption by investigating whether comparable long-range performance can be achieved on the standard latitude-longitude grid. We introduce AtmosMJ, a deep convolutional network that operates directly on ERA5 data without any spherical remapping. The model's stability is enabled by a novel Gated Residual Fusion (GRF) mechanism, which adaptively moderates feature updates to prevent error accumulation over long recursive simulations. Our results demonstrate that AtmosMJ produces stable and physically plausible forecasts for about 500 days. In quantitative evaluations, it achieves competitive 10-day forecast accuracy against models like Pangu-Weather and GraphCast, all while requiring a remarkably low training budget of 5.7 days on a V100 GPU. Our findings suggest that efficient architectural design, rather than non-standard data representation, can be the key to unlocking stable and computationally efficient long-range weather prediction.

