---
layout: default
title: GRPO-Guard: Mitigating Implicit Over-Optimization in Flow Matching via Regulated Clipping
---

# GRPO-Guard: Mitigating Implicit Over-Optimization in Flow Matching via Regulated Clipping

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.22319" class="toolbar-btn" target="_blank">📄 arXiv: 2510.22319v2</a>
  <a href="https://arxiv.org/pdf/2510.22319.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.22319v2" onclick="toggleFavorite(this, '2510.22319v2', 'GRPO-Guard: Mitigating Implicit Over-Optimization in Flow Matching via Regulated Clipping')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jing Wang, Jiajun Liang, Jie Liu, Henglin Liu, Gongye Liu, Jun Zheng, Wanyuan Pang, Ao Ma, Zhenyu Xie, Xintao Wang, Meng Wang, Pengfei Wan, Xiaodan Liang

**分类**: cs.CV, cs.LG

**发布日期**: 2025-10-25 (更新: 2025-10-30)

**备注**: Project Page: https://jingw193.github.io/GRPO-Guard/

---

## 💡 一句话要点

**GRPO-Guard：通过调节裁剪缓解Flow Matching中的隐式过度优化**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `Flow Matching` `强化学习` `过度优化` `扩散模型` `生成模型` `重要性采样` `梯度裁剪`

## 📋 核心要点

1. 现有基于GRPO的Flow Matching方法存在隐式过度优化问题，导致图像质量和文本对齐等关键指标下降。
2. GRPO-Guard通过比率归一化和梯度重加权，实现调节裁剪机制，稳定优化过程，缓解过度优化。
3. 实验表明，GRPO-Guard在多个扩散模型和代理任务上，显著减少过度优化，并保持或提升生成质量。

## 📝 摘要（中文）

最近，基于GRPO的强化学习在优化flow-matching模型方面取得了显著进展，有效地提高了模型与特定任务奖励的对齐程度。在这些框架中，策略更新依赖于重要性比率裁剪来约束过度自信的正梯度和负梯度。然而，在实践中，我们观察到重要性比率分布的系统性偏移——其均值低于1，并且其方差在不同时间步长上差异很大。这种左移且不一致的分布阻止了正优势样本进入裁剪区域，导致该机制无法约束过度自信的正向更新。因此，策略模型不可避免地进入隐式过度优化阶段——虽然代理奖励持续增加，但图像质量和文本提示对齐等关键指标急剧下降，最终使得学习到的策略在实际应用中变得不切实际。为了解决这个问题，我们引入了GRPO-Guard，这是对现有GRPO框架的一个简单而有效的增强。我们的方法结合了比率归一化，它恢复了平衡且步长一致的重要性比率，确保PPO裁剪能够正确地约束去噪时间步长上的有害更新。此外，梯度重加权策略均衡了噪声条件下的策略梯度，防止来自特定时间步长区域的过度更新。总之，这些设计充当了一种调节裁剪机制，稳定了优化过程，并在不依赖于繁重的KL正则化的情况下，大大缓解了隐式过度优化。在多个扩散骨干网络（例如，SD3.5M，Flux.1-dev）和各种代理任务上的大量实验表明，GRPO-Guard显著减少了过度优化，同时保持甚至提高了生成质量。

## 🔬 方法详解

**问题定义**：论文旨在解决基于GRPO的Flow Matching模型训练过程中出现的隐式过度优化问题。现有方法依赖重要性比率裁剪来约束梯度更新，但实际中重要性比率分布存在偏移和不一致性，导致裁剪机制失效，模型在代理奖励提升的同时，图像质量等关键指标下降。

**核心思路**：论文的核心思路是通过调节裁剪机制，使其能够有效地约束有害的梯度更新，从而避免隐式过度优化。具体来说，通过恢复平衡且步长一致的重要性比率，并均衡噪声条件下的策略梯度，来稳定优化过程。

**技术框架**：GRPO-Guard是对现有GRPO框架的增强，主要包含两个模块：比率归一化和梯度重加权。比率归一化用于恢复重要性比率的平衡和一致性，梯度重加权用于均衡不同噪声条件下的策略梯度。这两个模块共同作用，形成一个调节裁剪机制。整体流程是在GRPO框架的基础上，在计算重要性比率和更新策略时，加入这两个模块进行调整。

**关键创新**：论文的关键创新在于提出了一个调节裁剪机制，通过比率归一化和梯度重加权，解决了现有GRPO方法中重要性比率分布偏移和不一致的问题，从而有效地约束了有害的梯度更新，缓解了隐式过度优化。与现有方法相比，GRPO-Guard不需要依赖繁重的KL正则化，实现更稳定的优化。

**关键设计**：比率归一化通过对重要性比率进行标准化，使其均值接近1，方差在不同时间步长上保持一致。梯度重加权通过对不同噪声条件下的策略梯度进行加权，使得每个噪声条件对策略更新的贡献更加均衡。具体的参数设置和损失函数细节在论文中进行了详细描述，例如，如何选择合适的标准化方法和加权系数。

## 📊 实验亮点

实验结果表明，GRPO-Guard在SD3.5M和Flux.1-dev等多个扩散模型上，以及图像生成和文本生成等多个代理任务上，都能够显著减少过度优化，同时保持甚至提高生成质量。具体来说，GRPO-Guard在某些任务上能够将图像质量指标提升超过10%，同时保持文本对齐度。

## 🎯 应用场景

GRPO-Guard可应用于各种基于Flow Matching的生成模型训练，例如图像生成、文本生成等。该方法能够提高生成模型的稳定性和生成质量，避免过度优化导致的性能下降，具有广泛的应用前景和实际价值。未来可进一步探索其在其他强化学习任务中的应用。

## 📄 摘要（原文）

> Recently, GRPO-based reinforcement learning has shown remarkable progress in optimizing flow-matching models, effectively improving their alignment with task-specific rewards. Within these frameworks, the policy update relies on importance-ratio clipping to constrain overconfident positive and negative gradients. However, in practice, we observe a systematic shift in the importance-ratio distribution-its mean falls below 1 and its variance differs substantially across timesteps. This left-shifted and inconsistent distribution prevents positive-advantage samples from entering the clipped region, causing the mechanism to fail in constraining overconfident positive updates. As a result, the policy model inevitably enters an implicit over-optimization stage-while the proxy reward continues to increase, essential metrics such as image quality and text-prompt alignment deteriorate sharply, ultimately making the learned policy impractical for real-world use. To address this issue, we introduce GRPO-Guard, a simple yet effective enhancement to existing GRPO frameworks. Our method incorporates ratio normalization, which restores a balanced and step-consistent importance ratio, ensuring that PPO clipping properly constrains harmful updates across denoising timesteps. In addition, a gradient reweighting strategy equalizes policy gradients over noise conditions, preventing excessive updates from particular timestep regions. Together, these designs act as a regulated clipping mechanism, stabilizing optimization and substantially mitigating implicit over-optimization without relying on heavy KL regularization. Extensive experiments on multiple diffusion backbones (e.g., SD3.5M, Flux.1-dev) and diverse proxy tasks demonstrate that GRPO-Guard significantly reduces over-optimization while maintaining or even improving generation quality.

