---
layout: default
title: From Language to Locomotion: Retargeting-free Humanoid Control via Motion Latent Guidance
---

# From Language to Locomotion: Retargeting-free Humanoid Control via Motion Latent Guidance

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.14952" target="_blank" class="toolbar-btn">arXiv: 2510.14952v2</a>
    <a href="https://arxiv.org/pdf/2510.14952.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.14952v2" 
            onclick="toggleFavorite(this, '2510.14952v2', 'From Language to Locomotion: Retargeting-free Humanoid Control via Motion Latent Guidance')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Zhe Li, Cheng Chi, Yangyang Wei, Boan Zhu, Yibo Peng, Tao Huang, Pengwei Wang, Zhongyuan Wang, Shanghang Zhang, Chang Xu

**分类**: cs.RO, cs.CV

**发布日期**: 2025-10-16 (更新: 2025-10-17)

---

## 💡 一句话要点

**RoboGhost：提出一种无重定向的语言引导人形机器人运动控制框架**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱四：生成式动作 (Generative Motion)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `人形机器人控制` `语言引导` `运动生成` `扩散模型` `无重定向` `Transformer` `运动潜在空间`

## 📋 核心要点

1. 现有语言引导的人形机器人运动控制流程繁琐且不可靠，易累积误差，延迟高，语义与控制耦合弱。
2. RoboGhost通过语言条件下的运动潜在空间引导，直接生成机器人动作，无需中间的运动解码和重定向步骤。
3. 实验表明，RoboGhost降低了延迟，提高了成功率和跟踪精度，并可扩展到图像、音频等多种模态。

## 📝 摘要（中文）

本文提出了一种名为RoboGhost的无重定向框架，用于直接根据语言引导人形机器人运动。该方法绕过了显式的运动解码和重定向过程，使基于扩散模型的策略能够直接从噪声中去噪生成可执行的动作，从而保留语义意图并支持快速、反应式的控制。混合因果Transformer-扩散运动生成器进一步确保了长时程的一致性，同时保持稳定性和多样性，为精确的人形机器人行为产生丰富的潜在表示。大量实验表明，RoboGhost显著降低了部署延迟，提高了成功率和跟踪精度，并在真实人形机器人上产生了平滑、语义对齐的运动。此外，该框架自然地扩展到其他模态，如图像、音频和音乐，为视觉-语言-动作人形机器人系统提供了一个通用的基础。

## 🔬 方法详解

**问题定义**：现有语言引导人形机器人运动控制方法通常需要先解码人类运动，然后将其重定向到机器人形态，最后通过基于物理的控制器进行跟踪。这种多阶段过程容易产生累积误差，引入高延迟，并且语义和控制之间的耦合较弱。因此，需要一种更直接的从语言到动作的路径，消除脆弱的中间阶段。

**核心思路**：RoboGhost的核心思路是绕过显式的运动解码和重定向步骤，直接根据语言信息生成机器人的动作。通过将语言信息映射到运动潜在空间，并利用扩散模型从噪声中生成可执行的动作，从而实现语义意图的保留和快速响应的控制。

**技术框架**：RoboGhost框架包含一个混合因果Transformer-扩散运动生成器和一个基于扩散模型的策略。首先，语言信息被输入到混合因果Transformer-扩散运动生成器中，生成运动潜在表示。然后，基于扩散模型的策略利用这些潜在表示，直接从噪声中去噪生成机器人的动作。整个框架避免了中间的运动解码和重定向步骤。

**关键创新**：RoboGhost最重要的技术创新点是无重定向的运动控制方法。与现有方法相比，RoboGhost直接根据语言信息生成机器人的动作，无需中间的运动解码和重定向步骤，从而降低了延迟，提高了精度，并增强了语义和控制之间的耦合。

**关键设计**：混合因果Transformer-扩散运动生成器采用混合架构，结合了因果Transformer和扩散模型，以确保长时程的一致性，同时保持稳定性和多样性。基于扩散模型的策略使用运动潜在表示作为条件，指导动作的生成。具体的损失函数和网络结构细节在论文中有详细描述（未知）。

## 📊 实验亮点

实验结果表明，RoboGhost显著降低了部署延迟，提高了成功率和跟踪精度。具体而言，RoboGhost在真实人形机器人上产生了平滑、语义对齐的运动，并且可以自然地扩展到其他模态，如图像、音频和音乐。具体的性能数据和对比基线在论文中有详细描述（未知）。

## 🎯 应用场景

RoboGhost框架可应用于各种需要语言引导的人形机器人控制任务，例如家庭服务机器人、工业机器人和搜救机器人。该框架还可以扩展到其他模态，如图像、音频和音乐，为视觉-语言-动作人形机器人系统提供一个通用的基础，从而实现更智能、更自然的人机交互。

## 📄 摘要（原文）

> Natural language offers a natural interface for humanoid robots, but existing language-guided humanoid locomotion pipelines remain cumbersome and untrustworthy. They typically decode human motion, retarget it to robot morphology, and then track it with a physics-based controller. However, this multi-stage process is prone to cumulative errors, introduces high latency, and yields weak coupling between semantics and control. These limitations call for a more direct pathway from language to action, one that eliminates fragile intermediate stages. Therefore, we present RoboGhost, a retargeting-free framework that directly conditions humanoid policies on language-grounded motion latents. By bypassing explicit motion decoding and retargeting, RoboGhost enables a diffusion-based policy to denoise executable actions directly from noise, preserving semantic intent and supporting fast, reactive control. A hybrid causal transformer-diffusion motion generator further ensures long-horizon consistency while maintaining stability and diversity, yielding rich latent representations for precise humanoid behavior. Extensive experiments demonstrate that RoboGhost substantially reduces deployment latency, improves success rates and tracking precision, and produces smooth, semantically aligned locomotion on real humanoids. Beyond text, the framework naturally extends to other modalities such as images, audio, and music, providing a universal foundation for vision-language-action humanoid systems.

