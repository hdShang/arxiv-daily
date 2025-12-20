---
layout: default
title: PolaRiS: Scalable Real-to-Sim Evaluations for Generalist Robot Policies
---

# PolaRiS: Scalable Real-to-Sim Evaluations for Generalist Robot Policies

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16881" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16881v1</a>
  <a href="https://arxiv.org/pdf/2512.16881.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16881v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16881v1', 'PolaRiS: Scalable Real-to-Sim Evaluations for Generalist Robot Policies')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Arhan Jain, Mingtong Zhang, Kanav Arora, William Chen, Marcel Torne, Muhammad Zubair Irshad, Sergey Zakharov, Yue Wang, Sergey Levine, Chelsea Finn, Wei-Chiu Ma, Dhruv Shah, Abhishek Gupta, Karl Pertsch

**分类**: cs.RO, cs.LG

**发布日期**: 2025-12-18

**备注**: Website: https://polaris-evals.github.io/

---

## 💡 一句话要点

**PolaRiS：用于通用机器人策略的可扩展真实到模拟评估框架**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `机器人学习` `仿真评估` `真实到模拟` `神经重建` `通用机器人策略` `领域自适应` `协同训练`

## 📋 核心要点

1. 机器人策略评估面临真实环境成本高、可重复性差的问题，现有仿真环境与真实环境存在较大差距，导致评估结果不准确。
2. PolaRiS通过神经重建将真实场景转化为交互式仿真环境，并结合仿真数据协同训练，缩小真实到模拟的差距，实现更可靠的策略评估。
3. 实验表明，PolaRiS评估与真实世界通用策略性能的相关性远高于现有仿真基准，能够快速创建多样化的仿真环境。

## 📝 摘要（中文）

机器人学习研究面临的一个重大挑战是准确测量和比较机器人策略的性能。由于真实世界rollout的随机性、可重复性和耗时性，机器人技术的基准测试历来具有挑战性。对于最近的通用策略，需要在各种场景和任务中进行评估，这使得挑战更加严峻。仿真评估为真实世界评估提供了一种可扩展的补充，但现有仿真基准与真实世界之间的视觉和物理领域差距使其成为不可靠的策略改进信号。此外，构建逼真且多样化的仿真环境传统上需要大量的人力和专业知识。为了弥合差距，我们引入了仿真中的策略评估和环境重建（PolaRiS），这是一个可扩展的真实到模拟框架，用于高保真仿真机器人评估。PolaRiS利用神经重建方法将真实世界场景的短视频扫描转换为交互式仿真环境。此外，我们开发了一种简单的仿真数据协同训练方法，弥合了剩余的真实到模拟差距，并实现了在未见过的仿真环境中的零样本评估。通过仿真和真实世界之间的广泛配对评估，我们证明PolaRiS评估比现有仿真基准更能提供与真实世界通用策略性能的更强相关性。它的简单性还能够快速创建多样化的仿真环境。因此，这项工作朝着为下一代机器人基础模型进行分布式和民主化的评估迈出了一步。

## 🔬 方法详解

**问题定义**：现有机器人策略评估，尤其是在通用机器人策略方面，面临着真实环境评估成本高昂、难以复现，以及现有仿真环境与真实环境存在较大视觉和物理差异的问题。这种差异导致在仿真环境中表现良好的策略，在真实环境中表现不佳，使得仿真评估的可靠性大打折扣。此外，构建逼真且多样化的仿真环境需要大量的人工和专业知识，限制了评估的规模和范围。

**核心思路**：PolaRiS的核心思路是通过神经重建技术，将真实世界的场景快速转化为高保真的仿真环境。这样既避免了手动构建仿真环境的繁琐过程，又保证了仿真环境与真实环境的相似性。此外，通过仿真数据协同训练，进一步缩小真实到模拟的差距，提高仿真评估的准确性和可靠性。

**技术框架**：PolaRiS框架主要包含两个阶段：环境重建和策略评估。首先，利用神经重建方法，如神经辐射场（NeRF）或类似技术，将真实场景的短视频扫描转化为可交互的3D仿真环境。然后，在这些重建的仿真环境中对机器人策略进行评估。为了进一步提高评估的准确性，PolaRiS还采用了仿真数据协同训练的方法，即在真实数据和仿真数据上联合训练策略，以弥合真实到模拟的差距。

**关键创新**：PolaRiS最重要的创新点在于其能够快速、自动地将真实场景转化为高保真的仿真环境，从而实现可扩展的真实到模拟的机器人策略评估。与传统的手动构建仿真环境相比，PolaRiS大大降低了构建成本和时间，并提高了仿真环境的真实性和多样性。此外，仿真数据协同训练进一步提高了评估的准确性和可靠性。

**关键设计**：PolaRiS的关键设计包括：1) 使用高质量的神经重建方法，以保证仿真环境的视觉逼真度；2) 设计有效的仿真数据协同训练策略，以弥合真实到模拟的差距；3) 采用标准化的评估指标和协议，以便于不同策略之间的比较和分析。具体的参数设置、损失函数和网络结构等技术细节取决于所使用的神经重建方法和协同训练策略，论文中可能包含更详细的描述。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16881v1/figures/Teaser_Karl_version.jpg" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16881v1/figures/polaris_pipeline.jpg" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16881v1/figures/scene_comp_gui.jpg" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，PolaRiS评估与真实世界通用策略性能的相关性远高于现有仿真基准。通过在多个真实场景中进行评估，PolaRiS能够更准确地预测策略在真实环境中的表现。此外，PolaRiS还展示了快速创建多样化仿真环境的能力，为大规模的机器人策略评估提供了可能。

## 🎯 应用场景

PolaRiS的应用场景广泛，包括机器人算法的开发、测试和验证，以及机器人基础模型的训练和评估。它可以用于各种机器人应用，如家庭服务机器人、工业机器人、自动驾驶等。通过PolaRiS，研究人员可以更快速、更经济地评估和改进机器人策略，加速机器人技术的发展和应用。

## 📄 摘要（原文）

> A significant challenge for robot learning research is our ability to accurately measure and compare the performance of robot policies. Benchmarking in robotics is historically challenging due to the stochasticity, reproducibility, and time-consuming nature of real-world rollouts. This challenge is exacerbated for recent generalist policies, which has to be evaluated across a wide variety of scenes and tasks. Evaluation in simulation offers a scalable complement to real world evaluations, but the visual and physical domain gap between existing simulation benchmarks and the real world has made them an unreliable signal for policy improvement. Furthermore, building realistic and diverse simulated environments has traditionally required significant human effort and expertise. To bridge the gap, we introduce Policy Evaluation and Environment Reconstruction in Simulation (PolaRiS), a scalable real-to-sim framework for high-fidelity simulated robot evaluation. PolaRiS utilizes neural reconstruction methods to turn short video scans of real-world scenes into interactive simulation environments. Additionally, we develop a simple simulation data co-training recipe that bridges remaining real-to-sim gaps and enables zero-shot evaluation in unseen simulation environments. Through extensive paired evaluations between simulation and the real world, we demonstrate that PolaRiS evaluations provide a much stronger correlation to real world generalist policy performance than existing simulated benchmarks. Its simplicity also enables rapid creation of diverse simulated environments. As such, this work takes a step towards distributed and democratized evaluation for the next generation of robotic foundation models.

