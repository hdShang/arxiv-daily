---
layout: default
title: "ComputerRL: Scaling End-to-End Online Reinforcement Learning for Computer Use Agents"
---

# ComputerRL: Scaling End-to-End Online Reinforcement Learning for Computer Use Agents

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.14040" class="toolbar-btn" target="_blank">📄 arXiv: 2508.14040v2</a>
  <a href="https://arxiv.org/pdf/2508.14040.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.14040v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.14040v2', 'ComputerRL: Scaling End-to-End Online Reinforcement Learning for Computer Use Agents')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hanyu Lai, Xiao Liu, Yanxiao Zhao, Han Xu, Hanchen Zhang, Bohao Jing, Yanyu Ren, Shuntian Yao, Yuxiao Dong, Jie Tang

**分类**: cs.AI

**发布日期**: 2025-08-19 (更新: 2025-10-21)

**🔗 代码/项目**: [GITHUB](https://github.com/thudm/ComputerRL)

---

## 💡 一句话要点

**提出ComputerRL以解决桌面智能代理的训练效率问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `桌面智能` `强化学习` `分布式训练` `API-GUI交互` `Entropulse策略` `自动化` `人机交互`

## 📋 核心要点

1. 现有的桌面智能代理在复杂环境中的操作效率低下，难以实现高效的在线强化学习训练。
2. 论文提出了ComputerRL框架，结合API-GUI范式和分布式强化学习基础设施，提升训练的可扩展性和稳健性。
3. 实验结果表明，AutoGLM-OS-9B在OSWorld基准上达到了48.9%的准确率，显著优于现有方法。

## 📝 摘要（中文）

我们介绍了ComputerRL，一个用于自主桌面智能的框架，使代理能够熟练操作复杂的数字工作空间。ComputerRL采用API-GUI范式，统一了程序化API调用和直接GUI交互，以解决机器代理与人类中心桌面环境之间的固有不匹配。为支持可扩展和稳健的训练，我们开发了一个分布式强化学习基础设施，能够协调数千个并行虚拟桌面环境，加速大规模在线强化学习。此外，我们提出了Entropulse训练策略，通过交替进行强化学习和监督微调，有效缓解了在长时间训练中出现的熵崩溃。我们在开放模型GLM-4-9B-0414和GLM-4.1V-9B-Thinking上应用ComputerRL，并在OSWorld基准上进行评估。AutoGLM-OS-9B达到了48.9%的新状态-of-the-art准确率，显著提升了桌面自动化中的通用代理性能。

## 🔬 方法详解

**问题定义**：本论文旨在解决桌面智能代理在复杂数字工作空间中进行高效在线强化学习训练的挑战。现有方法在环境效率和训练稳定性方面存在不足，导致训练效果不理想。

**核心思路**：论文的核心思路是通过引入API-GUI范式，统一程序化API调用与GUI交互，解决机器代理与人类用户之间的交互不匹配问题。同时，开发分布式强化学习基础设施以支持大规模训练。

**技术框架**：ComputerRL框架包括多个主要模块：API-GUI交互模块、分布式训练基础设施、Entropulse训练策略等。通过协调数千个虚拟桌面环境，实现高效的在线强化学习。

**关键创新**：最重要的技术创新是Entropulse训练策略，它通过交替进行强化学习和监督微调，有效缓解了长时间训练中的熵崩溃现象。这一策略显著提高了训练的稳定性和效率。

**关键设计**：在设计中，采用了分布式架构以支持并行训练，设置了适当的超参数以优化训练过程，并设计了损失函数以平衡强化学习与监督学习的目标。

## 📊 实验亮点

实验结果显示，AutoGLM-OS-9B在OSWorld基准上达到了48.9%的准确率，创下了新的状态-of-the-art表现，相较于之前的基线有显著提升。这一成果展示了ComputerRL在桌面自动化领域的有效性和潜力。

## 🎯 应用场景

该研究的潜在应用领域包括桌面自动化、智能助手和人机交互等。通过提高桌面智能代理的训练效率，ComputerRL能够在实际工作环境中实现更高效的任务执行，提升用户体验。未来，该框架可能推动更多智能应用的开发与普及。

## 📄 摘要（原文）

> We introduce ComputerRL, a framework for autonomous desktop intelligence that enables agents to operate complex digital workspaces skillfully. ComputerRL features the API-GUI paradigm, which unifies programmatic API calls and direct GUI interaction to address the inherent mismatch between machine agents and human-centric desktop environments. Scaling end-to-end RL training is crucial for improvement and generalization across diverse desktop tasks; however, it remains challenging due to environmental inefficiency and instability during extended training. To support scalable and robust training, we develop a distributed RL infrastructure capable of orchestrating thousands of parallel virtual desktop environments to accelerate large-scale online RL. Furthermore, we propose Entropulse, a training strategy that alternates reinforcement learning with supervised fine-tuning, effectively mitigating entropy collapse during extended training runs. We employ ComputerRL on open models GLM-4-9B-0414 and GLM-4.1V-9B-Thinking, and evaluate them on the OSWorld benchmark. The AutoGLM-OS-9B achieves a new state-of-the-art accuracy of 48.9%, demonstrating significant improvements for general agents in desktop automation. Our code and the new OfficeWorld benchmark are available at https://github.com/thudm/ComputerRL. The algorithm and framework are adopted in building AutoGLM (Liu et al., 2024b).

