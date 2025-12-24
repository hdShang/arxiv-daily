---
layout: default
title: "UMI-on-Air: Embodiment-Aware Guidance for Embodiment-Agnostic Visuomotor Policies"
---

# UMI-on-Air: Embodiment-Aware Guidance for Embodiment-Agnostic Visuomotor Policies

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.02614" class="toolbar-btn" target="_blank">📄 arXiv: 2510.02614v2</a>
  <a href="https://arxiv.org/pdf/2510.02614.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.02614v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.02614v2', 'UMI-on-Air: Embodiment-Aware Guidance for Embodiment-Agnostic Visuomotor Policies')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Harsh Gupta, Xiaofeng Guo, Huy Ha, Chuer Pan, Muqing Cao, Dongjae Lee, Sebastian Scherer, Shuran Song, Guanya Shi

**分类**: cs.RO

**发布日期**: 2025-10-02 (更新: 2025-12-06)

**备注**: Result videos can be found at umi-on-air.github.io

---

## 💡 一句话要点

**UMI-on-Air：提出具身感知引导的通用操作策略，解决空中机器人操作难题。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `机器人操作` `具身智能` `扩散模型` `空中机器人` `模仿学习`

## 📋 核心要点

1. 现有方法难以将通用操作策略迁移到动力学受限的机器人上，导致性能下降。
2. 提出具身感知扩散策略（EADP），结合高层UMI策略和低层具身特定控制器，实现动态可行轨迹生成。
3. 实验表明，该方法在空中操作任务中提高了成功率、效率和鲁棒性，并能泛化到新环境。

## 📝 摘要（中文）

本文介绍了一种名为UMI-on-Air的框架，用于实现具身无关的操作策略的具身感知部署。该方法利用手持夹具（UMI）收集的各种无约束的人类演示来训练可泛化的视觉运动策略。将这些策略转移到受约束的机器人（如空中机械臂）上的一个核心挑战是控制和机器人动力学的不匹配，这通常会导致分布外行为和较差的执行效果。为了解决这个问题，我们提出了具身感知扩散策略（EADP），它在推理时将高级UMI策略与低级具身特定控制器相结合。通过将来自控制器跟踪成本的梯度反馈集成到扩散采样过程中，我们的方法引导轨迹生成朝着为部署的具身量身定制的动态可行模式发展。这使得在测试时能够进行即插即用的、具身感知的轨迹调整。我们在多个长时程和高精度空中操作任务上验证了我们的方法，与无引导的扩散基线相比，在扰动下显示出更高的成功率、效率和鲁棒性。最后，我们展示了在以前未见过的环境中部署，使用在野外收集的UMI演示，突出了跨各种（甚至高度约束的）具身扩展通用操作技能的实用途径。所有代码、数据和检查点将在接受后公开发布。

## 🔬 方法详解

**问题定义**：现有方法难以将通过人类演示学习到的通用操作策略有效地迁移到具有不同动力学特性的机器人平台上，尤其是像空中机器人这样具有严格动力学约束的平台。直接应用这些策略会导致机器人行为超出其安全或可行范围，从而导致任务失败。现有方法缺乏对具体机器人形态的感知和适应能力。

**核心思路**：核心思路是将一个通用的、通过人类演示学习到的高层策略（UMI策略）与一个低层的、针对特定机器人形态的控制器相结合。通过在扩散采样过程中融入来自低层控制器的梯度反馈，引导轨迹生成过程，使其生成的轨迹更符合特定机器人的动力学约束，从而实现具身感知的轨迹调整。

**技术框架**：UMI-on-Air框架包含两个主要组成部分：一个通过人类演示学习到的通用操作策略（UMI策略），以及一个针对特定机器人形态的低层控制器。在推理阶段，首先使用UMI策略生成一个初始轨迹，然后将该轨迹输入到低层控制器中。控制器计算跟踪成本的梯度，并将该梯度反馈到扩散采样过程中，从而引导轨迹生成朝着动态可行的方向发展。最终，控制器执行调整后的轨迹。

**关键创新**：关键创新在于Embodiment-Aware Diffusion Policy (EADP)，它将高层通用策略与低层具身特定控制器相结合，并通过梯度反馈机制实现轨迹的动态调整。这种方法能够在推理阶段根据具体机器人的动力学特性对轨迹进行优化，从而提高策略的泛化能力和鲁棒性。

**关键设计**：EADP使用扩散模型生成轨迹，并通过将低层控制器的跟踪成本梯度注入到扩散采样过程中来引导轨迹生成。具体的损失函数设计和网络结构细节（例如扩散模型的具体架构、梯度注入的方式等）在论文中可能有所描述，但摘要中未明确提及。控制器的具体设计取决于目标机器人平台。

## 📊 实验亮点

实验结果表明，UMI-on-Air框架在多个长时程和高精度空中操作任务中，与无引导的扩散基线相比，显著提高了成功率、效率和鲁棒性。在扰动环境下，该方法表现出更强的抗干扰能力。此外，该方法还能够在以前未见过的环境中进行部署，展示了良好的泛化能力。

## 🎯 应用场景

该研究成果可应用于各种机器人操作任务，尤其是在需要将通用操作技能迁移到具有不同动力学特性的机器人平台上的场景。例如，可用于空中机器人进行高精度操作、灾后救援、环境监测等任务，也可用于地面机器人在复杂环境中的操作任务。该方法具有很高的实际应用价值，能够降低机器人开发的成本和难度。

## 📄 摘要（原文）

> We introduce UMI-on-Air, a framework for embodiment-aware deployment of embodiment-agnostic manipulation policies. Our approach leverages diverse, unconstrained human demonstrations collected with a handheld gripper (UMI) to train generalizable visuomotor policies. A central challenge in transferring these policies to constrained robotic embodiments-such as aerial manipulators-is the mismatch in control and robot dynamics, which often leads to out-of-distribution behaviors and poor execution. To address this, we propose Embodiment-Aware Diffusion Policy (EADP), which couples a high-level UMI policy with a low-level embodiment-specific controller at inference time. By integrating gradient feedback from the controller's tracking cost into the diffusion sampling process, our method steers trajectory generation towards dynamically feasible modes tailored to the deployment embodiment. This enables plug-and-play, embodiment-aware trajectory adaptation at test time. We validate our approach on multiple long-horizon and high-precision aerial manipulation tasks, showing improved success rates, efficiency, and robustness under disturbances compared to unguided diffusion baselines. Finally, we demonstrate deployment in previously unseen environments, using UMI demonstrations collected in the wild, highlighting a practical pathway for scaling generalizable manipulation skills across diverse-and even highly constrained-embodiments. All code, data, and checkpoints will be publicly released after acceptance. Result videos can be found at umi-on-air.github.io.

