---
layout: default
title: A Goal-Oriented Reinforcement Learning-Based Path Planning Algorithm for Modular Self-Reconfigurable Satellites
---

# A Goal-Oriented Reinforcement Learning-Based Path Planning Algorithm for Modular Self-Reconfigurable Satellites

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.01966" class="toolbar-btn" target="_blank">📄 arXiv: 2505.01966v2</a>
  <a href="https://arxiv.org/pdf/2505.01966.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.01966v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.01966v2', 'A Goal-Oriented Reinforcement Learning-Based Path Planning Algorithm for Modular Self-Reconfigurable Satellites')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Bofei Liu, Dong Ye, Zunhao Yao, Zhaowei Sun

**分类**: cs.RO, cs.AI, cs.LG

**发布日期**: 2025-05-04 (更新: 2025-07-22)

**备注**: 6 pages, 7 figures

---

## 💡 一句话要点

**提出基于目标导向强化学习的路径规划算法以解决模块化自重构卫星问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `模块化卫星` `路径规划` `强化学习` `自重构` `多目标配置` `稀疏奖励` `无效动作屏蔽` `后见经验重放`

## 📋 核心要点

1. 现有的路径规划算法在处理模块化自重构卫星的多目标配置时，面临计算复杂度高和泛化能力差的问题。
2. 本文提出了一种目标导向的强化学习路径规划算法，首次解决了处理多个目标配置的挑战，并引入了后见经验重放和无效动作屏蔽技术。
3. 实验结果显示，该算法在四个和六个单元的模块化卫星集群中，成功率分别达到95%和73%，显著提升了路径规划的有效性。

## 📝 摘要（中文）

模块化自重构卫星是由多个独立模块单元组成的卫星集群，能够改变其配置以执行多样化的任务和使命目标。现有的重构路径规划算法常面临计算复杂度高、泛化能力差以及对多样化目标配置支持有限等挑战。为了解决这些问题，本文提出了一种基于目标导向的强化学习路径规划算法。这是首个解决以往强化学习方法无法处理多个目标配置的挑战的算法。此外，论文还引入了后见经验重放和无效动作屏蔽等技术，以克服稀疏奖励和无效动作带来的重大障碍。基于这些设计，模型在由四个和六个单元组成的模块化卫星集群中，分别达到了95%和73%的成功率。

## 🔬 方法详解

**问题定义**：本文旨在解决模块化自重构卫星在路径规划中面临的高计算复杂度、泛化能力差以及对多目标配置支持不足等问题。现有方法在处理多个目标配置时表现不佳，导致任务执行效率低下。

**核心思路**：论文提出的目标导向强化学习算法通过引入后见经验重放和无效动作屏蔽技术，旨在有效应对稀疏奖励和无效动作的挑战，从而提高路径规划的成功率和效率。

**技术框架**：整体架构包括环境建模、状态表示、动作选择和奖励机制等模块。算法通过强化学习框架进行训练，利用历史经验优化决策过程。

**关键创新**：该算法的主要创新在于首次实现了对多个目标配置的有效处理，克服了以往方法在多目标路径规划中的局限性，显著提升了任务执行的灵活性和效率。

**关键设计**：在算法设计中，采用了特定的损失函数来平衡探索与利用，设置了合适的超参数以优化学习过程，并设计了网络结构以适应复杂的状态空间和动作空间。通过这些设计，算法能够更好地适应模块化卫星的动态环境。

## 📊 实验亮点

实验结果表明，所提出的算法在模块化卫星集群中表现优异，四个单元的成功率达到95%，六个单元的成功率为73%。相比于传统方法，该算法在处理多目标配置时显著提升了路径规划的成功率，展示了其在实际应用中的巨大潜力。

## 🎯 应用场景

该研究的潜在应用领域包括卫星群的自主重构、空间任务的动态调度以及复杂环境下的路径规划等。通过提高模块化卫星的任务执行效率，该算法能够在未来的空间探索和卫星通信中发挥重要作用，推动智能卫星技术的发展。

## 📄 摘要（原文）

> Modular self-reconfigurable satellites refer to satellite clusters composed of individual modular units capable of altering their configurations. The configuration changes enable the execution of diverse tasks and mission objectives. Existing path planning algorithms for reconfiguration often suffer from high computational complexity, poor generalization capability, and limited support for diverse target configurations. To address these challenges, this paper proposes a goal-oriented reinforcement learning-based path planning algorithm. This algorithm is the first to address the challenge that previous reinforcement learning methods failed to overcome, namely handling multiple target configurations. Moreover, techniques such as Hindsight Experience Replay and Invalid Action Masking are incorporated to overcome the significant obstacles posed by sparse rewards and invalid actions. Based on these designs, our model achieves a 95% and 73% success rate in reaching arbitrary target configurations in a modular satellite cluster composed of four and six units, respectively.

