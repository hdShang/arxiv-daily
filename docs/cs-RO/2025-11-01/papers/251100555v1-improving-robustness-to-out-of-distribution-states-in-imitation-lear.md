---
layout: default
title: Improving Robustness to Out-of-Distribution States in Imitation Learning via Deep Koopman-Boosted Diffusion Policy
---

# Improving Robustness to Out-of-Distribution States in Imitation Learning via Deep Koopman-Boosted Diffusion Policy

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.00555" class="toolbar-btn" target="_blank">📄 arXiv: 2511.00555v1</a>
  <a href="https://arxiv.org/pdf/2511.00555.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.00555v1" onclick="toggleFavorite(this, '2511.00555v1', 'Improving Robustness to Out-of-Distribution States in Imitation Learning via Deep Koopman-Boosted Diffusion Policy')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Dianye Huang, Nassir Navab, Zhongliang Jiang

**分类**: cs.RO

**发布日期**: 2025-11-01

**备注**: Accepted by IEEE T-RO

**DOI**: [10.1109/TRO.2025.3629819](https://doi.org/10.1109/TRO.2025.3629819)

**🔗 代码/项目**: [GITHUB](https://github.com/dianyeHuang/D3P)

---

## 💡 一句话要点

**提出D3P算法，通过深度Koopman增强扩散策略提升模仿学习在分布外状态的鲁棒性**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `模仿学习` `扩散模型` `机器人操作` `Koopman算子` `分布外泛化`

## 📋 核心要点

1. 现有基于扩散的模仿学习方法难以捕捉长时依赖，尤其是在融合本体感受信息时，易过拟合。
2. D3P算法通过双分支架构解耦视觉和本体感受信息，并引入Koopman算子增强视觉表征学习。
3. 实验结果表明，D3P在仿真和真实机器人任务中均优于现有扩散策略，平均提升超过14%。

## 📝 摘要（中文）

本文提出了一种深度Koopman增强双分支扩散策略(D3P)算法，旨在提高模仿学习在机器人操作任务中对分布外状态的鲁棒性。现有基于扩散模型的范式难以捕捉跨多步骤的强时间依赖性，尤其是在融合本体感受输入时，容易过度拟合本体感受线索而忽略视觉特征。D3P引入双分支架构，解耦不同感觉模态组合的作用：视觉分支编码视觉观测以指示任务进度，融合分支整合视觉和本体感受输入以进行精确操作。当机器人未能完成中间目标时，策略可以动态切换到视觉分支生成的动作块，恢复到先前观察到的状态并重新尝试任务。此外，D3P还结合了深度Koopman算子模块，以增强视觉表征学习。在推理过程中，使用生成模型的测试时损失作为置信度信号，指导时间重叠的预测动作块的聚合，从而提高策略执行的可靠性。在六个RLBench桌面任务的仿真实验中，D3P的性能优于最先进的扩散策略，平均提升14.6%。在三个真实机器人操作任务中，实现了15.0%的改进。

## 🔬 方法详解

**问题定义**：现有基于扩散模型的模仿学习方法在机器人操作任务中，难以有效捕捉长时时间依赖关系，尤其是在融合视觉和本体感受信息时。策略容易过度依赖本体感受信息，而忽略视觉信息提供的任务进度指示，导致对分布外状态的泛化能力不足，例如在抓取失败后无法有效恢复。

**核心思路**：D3P的核心思路是解耦视觉和本体感受信息的作用，利用视觉信息作为任务进度的指示器，本体感受信息用于精确操作。通过双分支架构实现这一解耦，并在视觉分支中引入Koopman算子学习视觉表征的动态特性，从而提高策略的鲁棒性和泛化能力。

**技术框架**：D3P算法采用双分支扩散策略架构。视觉分支仅接收视觉输入，用于生成指示任务进度的动作块；融合分支接收视觉和本体感受输入，用于生成精确操作的动作块。当融合分支执行失败时，策略可以切换到视觉分支生成的动作块，尝试恢复到之前的状态。此外，D3P还包含一个深度Koopman算子模块，用于学习视觉输入的动态特性，并提供更鲁棒的视觉表征。推理阶段，利用生成模型的测试时损失作为置信度信号，指导时间重叠的预测动作块的聚合。

**关键创新**：D3P的关键创新在于：1) 双分支架构，解耦视觉和本体感受信息的作用；2) 引入深度Koopman算子，学习视觉表征的动态特性；3) 利用生成模型的测试时损失作为置信度信号，指导动作块的聚合。这些创新使得D3P能够更好地捕捉长时依赖关系，提高对分布外状态的鲁棒性。

**关键设计**：D3P的关键设计包括：1) 双分支扩散模型的具体网络结构，包括视觉分支和融合分支的网络层数、激活函数等；2) 深度Koopman算子模块的具体实现，包括Koopman算子的维度、损失函数等；3) 测试时损失的具体计算方式，以及如何利用该损失来指导动作块的聚合；4) 动作块的长度和重叠程度，以及如何选择合适的动作块长度以平衡精度和效率。

## 📊 实验亮点

D3P算法在六个RLBench桌面任务的仿真实验中，平均性能优于最先进的扩散策略14.6%。在三个真实机器人操作任务中，D3P算法的性能提升了15.0%。这些实验结果表明，D3P算法能够有效提高模仿学习在机器人操作任务中对分布外状态的鲁棒性。

## 🎯 应用场景

D3P算法可应用于各种机器人操作任务，尤其是在复杂、动态的环境中。例如，它可以用于家庭服务机器人，帮助机器人完成各种家务任务；也可以用于工业机器人，提高机器人在生产线上的灵活性和适应性。此外，该算法还可以应用于自动驾驶领域，提高自动驾驶系统在复杂交通环境中的鲁棒性。

## 📄 摘要（原文）

> Integrating generative models with action chunking has shown significant promise in imitation learning for robotic manipulation. However, the existing diffusion-based paradigm often struggles to capture strong temporal dependencies across multiple steps, particularly when incorporating proprioceptive input. This limitation can lead to task failures, where the policy overfits to proprioceptive cues at the expense of capturing the visually derived features of the task. To overcome this challenge, we propose the Deep Koopman-boosted Dual-branch Diffusion Policy (D3P) algorithm. D3P introduces a dual-branch architecture to decouple the roles of different sensory modality combinations. The visual branch encodes the visual observations to indicate task progression, while the fused branch integrates both visual and proprioceptive inputs for precise manipulation. Within this architecture, when the robot fails to accomplish intermediate goals, such as grasping a drawer handle, the policy can dynamically switch to execute action chunks generated by the visual branch, allowing recovery to previously observed states and facilitating retrial of the task. To further enhance visual representation learning, we incorporate a Deep Koopman Operator module that captures structured temporal dynamics from visual inputs. During inference, we use the test-time loss of the generative model as a confidence signal to guide the aggregation of the temporally overlapping predicted action chunks, thereby enhancing the reliability of policy execution. In simulation experiments across six RLBench tabletop tasks, D3P outperforms the state-of-the-art diffusion policy by an average of 14.6\%. On three real-world robotic manipulation tasks, it achieves a 15.0\% improvement. Code: https://github.com/dianyeHuang/D3P.

