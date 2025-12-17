---
layout: default
title: LikePhys: Evaluating Intuitive Physics Understanding in Video Diffusion Models via Likelihood Preference
---

# LikePhys: Evaluating Intuitive Physics Understanding in Video Diffusion Models via Likelihood Preference

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.11512" class="toolbar-btn" target="_blank">📄 arXiv: 2510.11512v2</a>
  <a href="https://arxiv.org/pdf/2510.11512.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.11512v2" onclick="toggleFavorite(this, '2510.11512v2', 'LikePhys: Evaluating Intuitive Physics Understanding in Video Diffusion Models via Likelihood Preference')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jianhao Yuan, Fabio Pizzati, Francesco Pinto, Lars Kunze, Ivan Laptev, Paul Newman, Philip Torr, Daniele De Martini

**分类**: cs.CV, cs.AI

**发布日期**: 2025-10-13 (更新: 2025-11-25)

**备注**: 22 pages, 9 figures

---

## 💡 一句话要点

**提出LikePhys，通过似然偏好评估视频扩散模型中的直观物理理解能力**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)**

**关键词**: `视频扩散模型` `直观物理理解` `评估方法` `似然偏好` `无监督学习`

## 📋 核心要点

1. 现有方法难以区分视频生成中物理合理性和视觉外观，导致难以准确评估视频扩散模型的直观物理理解能力。
2. LikePhys利用去噪目标作为ELBO似然代理，通过区分物理有效和无效视频来评估模型，无需额外训练。
3. 实验表明，提出的合理性偏好误差（PPE）与人类偏好高度一致，并在多个物理场景中优于现有评估方法。

## 📝 摘要（中文）

视频扩散模型中的直观物理理解能力对于构建通用的、物理上合理的现实世界模拟器至关重要。然而，由于难以区分生成结果中的物理正确性和视觉外观，准确评估这种能力仍然是一个挑战。为此，我们引入LikePhys，这是一种无需训练的方法，它通过使用去噪目标作为基于ELBO的似然代理，区分物理上有效和无效的视频，从而评估视频扩散模型中的直观物理。通过在我们构建的包含四个物理领域中十二个场景的基准上进行测试，我们表明我们的评估指标，合理性偏好误差（PPE），表现出与人类偏好很强的一致性，优于最先进的评估器基线。然后，我们系统地评估了当前视频扩散模型中的直观物理理解能力。我们的研究进一步分析了模型设计和推理设置如何影响直观物理理解，并强调了跨物理定律的特定领域能力差异。实证结果表明，尽管当前模型在复杂和混沌动力学方面存在困难，但随着模型容量和推理设置的扩展，物理理解能力有明显的提高趋势。

## 🔬 方法详解

**问题定义**：现有视频扩散模型在生成视频时，虽然视觉效果逼真，但其对物理世界的理解程度难以评估。现有评估方法难以区分视觉效果和物理合理性，缺乏有效的评估指标。因此，如何准确评估视频扩散模型对直观物理的理解能力是一个关键问题。

**核心思路**：LikePhys的核心思想是利用视频扩散模型的去噪过程来评估其对物理世界的理解。具体来说，该方法假设如果模型更好地理解物理规律，那么它会更倾向于给物理上合理的视频更高的似然估计。通过比较模型对物理有效和无效视频的似然估计，可以推断出模型对物理世界的理解程度。

**技术框架**：LikePhys的整体框架包括以下几个步骤：1）构建包含物理有效和无效视频对的数据集；2）使用视频扩散模型对数据集中的视频进行去噪；3）利用去噪过程中的损失函数作为ELBO似然的代理，计算模型对每个视频的似然估计；4）计算合理性偏好误差（PPE），即模型对无效视频的似然估计高于有效视频的比例，作为评估指标。

**关键创新**：LikePhys的关键创新在于提出了一种无需训练的评估方法，它利用视频扩散模型自身的去噪过程来评估其对物理世界的理解。与需要额外训练评估器的方法相比，LikePhys更加高效且易于实现。此外，该方法还提出了一种新的评估指标PPE，能够更好地反映模型对物理世界的理解程度。

**关键设计**：LikePhys的关键设计包括：1）使用去噪过程中的损失函数作为ELBO似然的代理，这是一种有效的近似方法；2）构建包含物理有效和无效视频对的数据集，保证了评估的准确性；3）使用合理性偏好误差（PPE）作为评估指标，能够更好地反映模型对物理世界的理解程度。具体来说，PPE的计算公式为：PPE = P(L_invalid > L_valid)，其中L_invalid和L_valid分别表示模型对无效和有效视频的似然估计。

## 📊 实验亮点

实验结果表明，LikePhys提出的合理性偏好误差（PPE）与人类偏好具有很强的一致性，优于现有的评估方法。在包含12个物理场景的基准测试中，LikePhys能够有效区分不同视频扩散模型在物理理解能力上的差异，并揭示了模型容量和推理设置对物理理解的影响。研究还发现，当前模型在处理复杂和混沌动力学方面仍存在挑战。

## 🎯 应用场景

该研究成果可应用于评估和改进视频扩散模型的物理合理性，从而提升其在现实世界模拟、游戏开发、机器人控制等领域的应用效果。通过LikePhys，研究人员可以更好地理解和优化视频生成模型，使其能够生成更符合物理规律的视频内容，从而提高用户体验和应用价值。

## 📄 摘要（原文）

> Intuitive physics understanding in video diffusion models plays an essential role in building general-purpose physically plausible world simulators, yet accurately evaluating such capacity remains a challenging task due to the difficulty in disentangling physics correctness from visual appearance in generation. To the end, we introduce LikePhys, a training-free method that evaluates intuitive physics in video diffusion models by distinguishing physically valid and impossible videos using the denoising objective as an ELBO-based likelihood surrogate on a curated dataset of valid-invalid pairs. By testing on our constructed benchmark of twelve scenarios spanning over four physics domains, we show that our evaluation metric, Plausibility Preference Error (PPE), demonstrates strong alignment with human preference, outperforming state-of-the-art evaluator baselines. We then systematically benchmark intuitive physics understanding in current video diffusion models. Our study further analyses how model design and inference settings affect intuitive physics understanding and highlights domain-specific capacity variations across physical laws. Empirical results show that, despite current models struggling with complex and chaotic dynamics, there is a clear trend of improvement in physics understanding as model capacity and inference settings scale.

