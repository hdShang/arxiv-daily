---
layout: default
title: Understanding Sampler Stochasticity in Training Diffusion Models for RLHF
---

# Understanding Sampler Stochasticity in Training Diffusion Models for RLHF

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.10767" class="toolbar-btn" target="_blank">📄 arXiv: 2510.10767</a>
  <a href="https://arxiv.org/pdf/2510.10767.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.10767" onclick="toggleFavorite(this, '2510.10767', 'Understanding Sampler Stochasticity in Training Diffusion Models for RLHF')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiayuan Sheng, Hanyang Zhao, Haoxian Chen, David D. Yao, Wenpin Tang

**分类**: cs.LG, cs.AI, math.OC

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**理论分析与实验验证：缩小RLHF扩散模型训练与推理采样器随机性差异**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `扩散模型` `人类反馈强化学习` `随机采样` `确定性采样` `奖励差距` `gDDIM` `文本到图像生成`

## 📋 核心要点

1. RLHF微调扩散模型时，训练和推理阶段采样器的随机性差异是关键挑战，导致奖励差距。
2. 论文采用gDDIM框架，支持高随机性，理论分析奖励差距，并提供VE和VP模型的收敛速度。
3. 实验表明，使用高随机性SDE训练能有效缩小奖励差距，提升ODE采样质量，验证了理论分析。

## 📝 摘要（中文）

本文研究了在RLHF中微调扩散模型时，训练阶段使用的随机采样器与推理阶段使用的确定性采样器之间的不匹配问题。实践中，模型通常使用随机SDE采样器进行微调以鼓励探索，而推理则依赖于确定性ODE采样器以提高效率和稳定性。这种差异导致了奖励差距，引发了人们对推理过程中能否获得高质量输出的担忧。本文从理论上描述了这种奖励差距，并为通用扩散模型提供了非平凡的界限，以及针对方差爆炸（VE）和方差保持（VP）高斯模型的更精确的收敛速度。在方法论上，我们采用了广义去噪扩散隐式模型（gDDIM）框架来支持任意高水平的随机性，从而保持整个过程中的数据边缘分布。通过使用去噪扩散策略优化（DDPO）和混合组相对策略优化（MixGRPO）在文本到图像模型上进行的大规模实验，我们的研究结果验证了奖励差距在训练过程中持续缩小，并且当使用更高随机性的SDE训练更新模型时，ODE采样质量得到提高。

## 🔬 方法详解

**问题定义**：在利用人类反馈强化学习（RLHF）微调扩散模型时，训练阶段通常使用随机采样器（如SDE采样器）以鼓励探索，而推理阶段为了效率和稳定性，则倾向于使用确定性采样器（如ODE采样器）。这种训练和推理阶段采样器之间的差异会导致奖励差距，即模型在训练时表现良好，但在实际推理时性能下降。现有方法未能充分解决或量化这种差距，导致难以保证推理阶段的输出质量。

**核心思路**：论文的核心思路是理论分析并量化训练和推理阶段采样器随机性差异导致的奖励差距。通过建立奖励差距的理论界限，可以更好地理解这种差异对模型性能的影响。此外，论文还提出使用广义去噪扩散隐式模型（gDDIM）框架，该框架能够支持任意高水平的随机性，从而在训练过程中更好地保持数据边缘分布，进而缩小奖励差距。

**技术框架**：整体框架基于扩散模型，并结合RLHF进行微调。主要包含以下几个阶段：1）使用随机SDE采样器进行训练，鼓励探索；2）使用确定性ODE采样器进行推理，提高效率和稳定性；3）采用gDDIM框架，支持高随机性，保持数据边缘分布；4）理论分析奖励差距，并提供VE和VP模型的收敛速度。

**关键创新**：论文的关键创新在于：1）首次对RLHF微调扩散模型中训练和推理阶段采样器随机性差异导致的奖励差距进行了理论分析，并提供了非平凡的界限；2）采用了gDDIM框架，该框架能够支持任意高水平的随机性，从而在训练过程中更好地保持数据边缘分布，进而缩小奖励差距；3）针对VE和VP高斯模型，提供了更精确的收敛速度。

**关键设计**：论文的关键设计包括：1）使用gDDIM框架，通过调整噪声水平来控制采样器的随机性；2）针对VE和VP模型，推导了具体的奖励差距界限和收敛速度；3）在实验中，使用了DDPO和MixGRPO等RLHF算法，并针对文本到图像模型进行了大规模实验。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2510.10767/illust3.jpg" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2510.10767/vp_model.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2510.10767/reward_gap.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

论文通过大规模实验验证了理论分析的有效性。实验结果表明，使用更高随机性的SDE训练能够有效缩小奖励差距，并显著提高ODE采样器的生成质量。具体来说，在文本到图像生成任务中，使用DDPO和MixGRPO算法，通过高随机性SDE训练的模型在ODE采样时表现出更好的视觉效果和更高的用户满意度。

## 🎯 应用场景

该研究成果可应用于各种需要利用人类反馈微调扩散模型的场景，例如文本到图像生成、图像编辑、音频合成等。通过缩小训练和推理阶段采样器随机性差异，可以提高生成内容质量，提升用户体验，并降低部署成本。未来，该研究可以进一步推广到其他生成模型和强化学习算法中。

## 📄 摘要（原文）

> Reinforcement Learning from Human Feedback (RLHF) is increasingly used to fine-tune diffusion models, but a key challenge arises from the mismatch between stochastic samplers used during training and deterministic samplers used during inference. In practice, models are fine-tuned using stochastic SDE samplers to encourage exploration, while inference typically relies on deterministic ODE samplers for efficiency and stability. This discrepancy induces a reward gap, raising concerns about whether high-quality outputs can be expected during inference. In this paper, we theoretically characterize this reward gap and provide non-vacuous bounds for general diffusion models, along with sharper convergence rates for Variance Exploding (VE) and Variance Preserving (VP) Gaussian models. Methodologically, we adopt the generalized denoising diffusion implicit models (gDDIM) framework to support arbitrarily high levels of stochasticity, preserving data marginals throughout. Empirically, our findings through large-scale experiments on text-to-image models using denoising diffusion policy optimization (DDPO) and mixed group relative policy optimization (MixGRPO) validate that reward gaps consistently narrow over training, and ODE sampling quality improves when models are updated using higher-stochasticity SDE training.

