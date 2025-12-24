---
layout: default
title: "PhysicalAgent: Towards General Cognitive Robotics with Foundation World Models"
---

# PhysicalAgent: Towards General Cognitive Robotics with Foundation World Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.13903" class="toolbar-btn" target="_blank">📄 arXiv: 2509.13903v1</a>
  <a href="https://arxiv.org/pdf/2509.13903.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.13903v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.13903v1', 'PhysicalAgent: Towards General Cognitive Robotics with Foundation World Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Artem Lykov, Jeffrin Sam, Hung Khang Nguyen, Vladislav Kozlovskiy, Yara Mahmoud, Valerii Serpiva, Miguel Altamirano Cabrera, Mikhail Konenkov, Dzmitry Tsetserukou

**分类**: cs.RO

**发布日期**: 2025-09-17

**备注**: submitted to IEEE conference

---

## 💡 一句话要点

**PhysicalAgent：基于世界模型的通用认知机器人框架，实现迭代推理和闭环执行。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱六：视频提取与匹配 (Video Extraction)**

**关键词**: `机器人操作` `世界模型` `视频生成` `扩散模型` `迭代推理` `闭环执行` `强化学习`

## 📋 核心要点

1. 现有机器人操作方法在泛化性和鲁棒性方面存在不足，难以应对复杂环境和任务。
2. PhysicalAgent通过生成视频演示、闭环执行和迭代重新规划，实现了更强的泛化和容错能力。
3. 实验表明，PhysicalAgent在多种机器人平台和感知模态下，显著优于现有方法，成功率高达83%。

## 📝 摘要（中文）

本文介绍了一种名为PhysicalAgent的机器人操作框架，它集成了迭代推理、基于扩散模型的视频生成和闭环执行。给定文本指令，该方法生成候选轨迹的短视频演示，在机器人上执行这些轨迹，并根据失败情况迭代地重新规划。这种方法能够从执行错误中稳健地恢复。我们在多种感知模态（自我中心、第三人称和模拟）和机器人平台（双臂UR3、Unitree G1人形机器人、模拟GR1）上评估了PhysicalAgent，并与最先进的特定任务基线进行比较。实验表明，我们的方法始终优于现有方法，在人类熟悉的任务中成功率高达83%。实际试验表明，首次尝试的成功率有限（20-30%），但迭代纠正将所有平台的总体成功率提高到80%。这些结果突出了基于视频的生成推理在通用机器人操作中的潜力，并强调了迭代执行对于从初始失败中恢复的重要性。我们的框架为可扩展、可适应和鲁棒的机器人控制铺平了道路。

## 🔬 方法详解

**问题定义**：现有机器人操作方法通常依赖于特定任务的训练数据，泛化能力差，难以适应新的环境和任务。此外，执行过程中出现的错误难以纠正，导致任务失败。因此，需要一种更通用、更鲁棒的机器人操作框架。

**核心思路**：PhysicalAgent的核心思路是利用世界模型进行视频生成，模拟机器人执行轨迹，并结合迭代推理和闭环执行，不断优化轨迹，从而提高任务成功率。通过视频生成，可以学习到更丰富的环境信息和动作模式，提高泛化能力。迭代推理和闭环执行则可以及时纠正错误，提高鲁棒性。

**技术框架**：PhysicalAgent的整体框架包括以下几个主要模块：1) 文本指令输入；2) 基于扩散模型的视频生成器，生成候选轨迹的视频演示；3) 机器人执行器，执行生成的轨迹；4) 状态感知模块，感知机器人和环境的状态；5) 迭代推理模块，根据状态感知结果和任务目标，重新规划轨迹。整个流程是一个闭环系统，不断迭代优化，直到任务成功或达到最大迭代次数。

**关键创新**：PhysicalAgent的关键创新在于将视频生成、迭代推理和闭环执行集成到一个统一的框架中。视频生成模块利用扩散模型，可以生成高质量的候选轨迹，为后续的推理和执行提供基础。迭代推理模块则可以根据实际执行情况，不断优化轨迹，提高任务成功率。

**关键设计**：视频生成模块采用扩散模型，通过学习大量的机器人操作视频数据，生成逼真的候选轨迹。迭代推理模块采用强化学习算法，根据状态感知结果和任务目标，学习最优的轨迹规划策略。闭环执行模块则采用PID控制算法，实现精确的机器人运动控制。

## 📊 实验亮点

PhysicalAgent在多个机器人平台和感知模态下进行了评估，实验结果表明，该方法始终优于现有方法，在人类熟悉的任务中成功率高达83%。实际试验表明，首次尝试的成功率有限（20-30%），但迭代纠正将所有平台的总体成功率提高到80%。这些结果验证了PhysicalAgent的有效性和鲁棒性。

## 🎯 应用场景

PhysicalAgent具有广泛的应用前景，可用于工业自动化、家庭服务、医疗康复等领域。例如，在工业自动化中，可以利用PhysicalAgent控制机器人完成复杂的装配任务；在家庭服务中，可以利用PhysicalAgent控制机器人完成家务劳动；在医疗康复中，可以利用PhysicalAgent辅助患者进行康复训练。该研究为通用机器人操作系统的发展奠定了基础。

## 📄 摘要（原文）

> We introduce PhysicalAgent, an agentic framework for robotic manipulation that integrates iterative reasoning, diffusion-based video generation, and closed-loop execution. Given a textual instruction, our method generates short video demonstrations of candidate trajectories, executes them on the robot, and iteratively re-plans in response to failures. This approach enables robust recovery from execution errors. We evaluate PhysicalAgent across multiple perceptual modalities (egocentric, third-person, and simulated) and robotic embodiments (bimanual UR3, Unitree G1 humanoid, simulated GR1), comparing against state-of-the-art task-specific baselines. Experiments demonstrate that our method consistently outperforms prior approaches, achieving up to 83% success on human-familiar tasks. Physical trials reveal that first-attempt success is limited (20-30%), yet iterative correction increases overall success to 80% across platforms. These results highlight the potential of video-based generative reasoning for general-purpose robotic manipulation and underscore the importance of iterative execution for recovering from initial failures. Our framework paves the way for scalable, adaptable, and robust robot control.

