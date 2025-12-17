---
layout: default
title: pi-Flow: Policy-Based Few-Step Generation via Imitation Distillation
---

# pi-Flow: Policy-Based Few-Step Generation via Imitation Distillation

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.14974" target="_blank" class="toolbar-btn">arXiv: 2510.14974v2</a>
    <a href="https://arxiv.org/pdf/2510.14974.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.14974v2" 
            onclick="toggleFavorite(this, '2510.14974v2', 'pi-Flow: Policy-Based Few-Step Generation via Imitation Distillation')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Hansheng Chen, Kai Zhang, Hao Tan, Leonidas Guibas, Gordon Wetzstein, Sai Bi

**分类**: cs.LG, cs.AI, cs.CV

**发布日期**: 2025-10-16 (更新: 2025-12-13)

**备注**: Code: https://github.com/Lakonik/piFlow Demos: https://huggingface.co/spaces/Lakonik/pi-Qwen \| https://huggingface.co/spaces/Lakonik/pi-FLUX.1 \| https://huggingface.co/spaces/Lakonik/pi-FLUX.2

---

## 💡 一句话要点

**提出π-Flow以解决少步生成模型的质量与多样性权衡问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `少步生成` `流模型` `模仿蒸馏` `生成对抗网络` `图像生成` `多样性提升` `质量优化`

## 📋 核心要点

1. 现有的少步生成模型在蒸馏过程中存在格式不匹配，导致复杂的训练过程和质量与多样性之间的权衡。
2. 本文提出的π-Flow通过修改学生模型的输出层，预测无网络策略，从而在未来子步骤中生成动态流速，简化了训练过程。
3. 在多个数据集上，π-Flow在保持高质量的同时，显著提高了生成样本的多样性，超越了现有最先进的模型。

## 📝 摘要（中文）

少步扩散或基于流的生成模型通常将预测速度的教师模型蒸馏为预测去噪数据捷径的学生模型。这种格式不匹配导致复杂的蒸馏过程，常常面临质量与多样性之间的权衡。为了解决这一问题，本文提出了基于策略的流模型（π-Flow）。π-Flow修改了学生流模型的输出层，使其在一个时间步长内预测无网络策略。该策略随后以微不足道的开销生成未来子步骤的动态流速，从而实现快速且准确的常微分方程（ODE）积分。为了使策略的ODE轨迹与教师模型匹配，本文引入了一种新颖的模仿蒸馏方法，通过标准的ℓ2流匹配损失将策略的速度与教师的速度沿着策略轨迹进行匹配。通过简单模仿教师的行为，π-Flow实现了稳定且可扩展的训练，避免了质量与多样性之间的权衡。在ImageNet 256²上，π-Flow达到了2.85的1-NFE FID，超越了相同DiT架构的先前1-NFE模型。在FLUX.1-12B和Qwen-Image-20B上，π-Flow在4个NFE时实现了显著更好的多样性，同时保持了教师级别的质量。

## 🔬 方法详解

**问题定义**：本文旨在解决现有少步生成模型在蒸馏过程中面临的格式不匹配问题，导致训练复杂且存在质量与多样性之间的权衡。

**核心思路**：π-Flow通过修改学生流模型的输出层，使其能够在一个时间步长内预测无网络策略，从而生成动态流速，简化了生成过程并提高了效率。

**技术框架**：整体架构包括教师模型和学生模型，学生模型通过模仿教师的行为进行训练。输出层的设计允许学生模型在未来子步骤中生成流速，而无需额外的网络评估。

**关键创新**：最重要的创新在于引入了模仿蒸馏方法，通过标准的ℓ2流匹配损失将策略的速度与教师的速度进行匹配，从而避免了质量与多样性之间的权衡。

**关键设计**：在参数设置上，使用了标准的ℓ2损失函数进行流匹配，网络结构上则采用了修改后的输出层设计，以支持无网络策略的生成。

## 📊 实验亮点

在ImageNet 256²上，π-Flow达到了2.85的1-NFE FID，超越了相同DiT架构的先前1-NFE模型。在FLUX.1-12B和Qwen-Image-20B上，π-Flow在4个NFE时实现了显著更好的多样性，同时保持了教师级别的质量，展示了其在生成任务中的优越性能。

## 🎯 应用场景

该研究的潜在应用领域包括图像生成、视频生成和其他需要高质量样本生成的任务。通过提高生成模型的多样性和质量，π-Flow有望在艺术创作、虚拟现实和游戏开发等领域产生深远影响。

## 📄 摘要（原文）

> Few-step diffusion or flow-based generative models typically distill a velocity-predicting teacher into a student that predicts a shortcut towards denoised data. This format mismatch has led to complex distillation procedures that often suffer from a quality-diversity trade-off. To address this, we propose policy-based flow models ($π$-Flow). $π$-Flow modifies the output layer of a student flow model to predict a network-free policy at one timestep. The policy then produces dynamic flow velocities at future substeps with negligible overhead, enabling fast and accurate ODE integration on these substeps without extra network evaluations. To match the policy's ODE trajectory to the teacher's, we introduce a novel imitation distillation approach, which matches the policy's velocity to the teacher's along the policy's trajectory using a standard $\ell_2$ flow matching loss. By simply mimicking the teacher's behavior, $π$-Flow enables stable and scalable training and avoids the quality-diversity trade-off. On ImageNet 256$^2$, it attains a 1-NFE FID of 2.85, outperforming previous 1-NFE models of the same DiT architecture. On FLUX.1-12B and Qwen-Image-20B at 4 NFEs, $π$-Flow achieves substantially better diversity than state-of-the-art DMD models, while maintaining teacher-level quality.

