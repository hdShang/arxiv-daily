---
layout: default
title: Certifying Stability of Reinforcement Learning Policies using Generalized Lyapunov Functions
---

# Certifying Stability of Reinforcement Learning Policies using Generalized Lyapunov Functions

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.10947" class="toolbar-btn" target="_blank">📄 arXiv: 2505.10947v3</a>
  <a href="https://arxiv.org/pdf/2505.10947.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.10947v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.10947v3', 'Certifying Stability of Reinforcement Learning Policies using Generalized Lyapunov Functions')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kehan Long, Jorge Cortés, Nikolay Atanasov

**分类**: cs.LG, cs.RO, eess.SY, math.OC

**发布日期**: 2025-05-16 (更新: 2025-12-06)

**备注**: NeurIPS 2025

---

## 💡 一句话要点

**提出基于广义李雅普诺夫函数的强化学习策略稳定性认证方法**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `强化学习` `李雅普诺夫函数` `稳定性认证` `神经网络` `控制理论` `多步损失` `系统安全`

## 📋 核心要点

1. 现有的李雅普诺夫方法在构建学习策略的稳定性证书时面临困难，限制了其在强化学习中的应用。
2. 本文提出通过增强RL值函数与神经网络残差项来学习广义李雅普诺夫函数，从而简化证书构建过程。
3. 实验结果表明，该方法在Gymnasium和DeepMind Control基准上成功认证了RL策略，并显著扩大了吸引域的近似范围。

## 📝 摘要（中文）

在强化学习（RL）策略下，为闭环系统建立稳定性证书是超越经验性能并提供系统行为保证的关键。传统的李雅普诺夫方法要求李雅普诺夫函数严格逐步减小，但对于学习的策略，这种证书的构建较为困难。本文首先研究线性二次调节器（LQR）问题，提出通过残差项增强LQR策略的值函数来获得李雅普诺夫函数，并放宽传统的李雅普诺夫减小要求，提出仅需在多个时间步上平均减小的广义李雅普诺夫条件。基于此，我们在非线性设置下提出了一种通过增强RL值函数与神经网络残差项来学习广义李雅普诺夫函数的方法。该方法成功认证了在Gymnasium和DeepMind Control基准上训练的RL策略，并扩展至联合训练神经控制器和稳定性证书，使用多步李雅普诺夫损失获得更大的吸引域内近似。整体而言，该方法为广泛的学习策略系统提供了稳定性认证的可能，促进了经典控制理论与现代学习方法的结合。

## 🔬 方法详解

**问题定义**：本文旨在解决在强化学习策略下闭环系统的稳定性认证问题。现有方法依赖于传统李雅普诺夫方法，难以为学习的策略构建有效的稳定性证书。

**核心思路**：论文提出通过将RL值函数与神经网络残差项结合，来学习广义李雅普诺夫函数，从而放宽传统李雅普诺夫减小要求，使得稳定性证书的构建更加简单。

**技术框架**：整体框架包括两个主要模块：首先，通过对LQR问题的分析，构建基于值函数的李雅普诺夫函数；其次，在非线性设置中，利用神经网络残差项增强值函数，学习广义李雅普诺夫函数。

**关键创新**：最重要的创新在于提出了广义李雅普诺夫条件，允许在多个时间步上平均减小，而非严格逐步减小，这一设计显著降低了稳定性证书的构建难度。

**关键设计**：在损失函数设计上，采用多步李雅普诺夫损失以联合训练神经控制器和稳定性证书，此外，网络结构上结合了神经网络以增强值函数的表达能力，提升了稳定性认证的效果。

## 📊 实验亮点

实验结果显示，所提出的方法在Gymnasium和DeepMind Control基准上成功认证了多个RL策略，并通过多步李雅普诺夫损失获得了比传统方法更大的吸引域内近似，提升幅度显著，验证了方法的有效性和实用性。

## 🎯 应用场景

该研究的潜在应用领域包括自动驾驶、机器人控制和智能制造等需要高可靠性和稳定性的系统。通过提供稳定性认证，该方法能够增强系统的安全性和可预测性，促进智能系统在实际环境中的应用与推广。

## 📄 摘要（原文）

> Establishing stability certificates for closed-loop systems under reinforcement learning (RL) policies is essential to move beyond empirical performance and offer guarantees of system behavior. Classical Lyapunov methods require a strict stepwise decrease in the Lyapunov function but such certificates are difficult to construct for learned policies. The RL value function is a natural candidate but it is not well understood how it can be adapted for this purpose. To gain intuition, we first study the linear quadratic regulator (LQR) problem and make two key observations. First, a Lyapunov function can be obtained from the value function of an LQR policy by augmenting it with a residual term related to the system dynamics and stage cost. Second, the classical Lyapunov decrease requirement can be relaxed to a generalized Lyapunov condition requiring only decrease on average over multiple time steps. Using this intuition, we consider the nonlinear setting and formulate an approach to learn generalized Lyapunov functions by augmenting RL value functions with neural network residual terms. Our approach successfully certifies the stability of RL policies trained on Gymnasium and DeepMind Control benchmarks. We also extend our method to jointly train neural controllers and stability certificates using a multi-step Lyapunov loss, resulting in larger certified inner approximations of the region of attraction compared to the classical Lyapunov approach. Overall, our formulation enables stability certification for a broad class of systems with learned policies by making certificates easier to construct, thereby bridging classical control theory and modern learning-based methods.

