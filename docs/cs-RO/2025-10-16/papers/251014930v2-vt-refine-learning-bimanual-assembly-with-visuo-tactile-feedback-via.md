---
layout: default
title: VT-Refine: Learning Bimanual Assembly with Visuo-Tactile Feedback via Simulation Fine-Tuning
---

# VT-Refine: Learning Bimanual Assembly with Visuo-Tactile Feedback via Simulation Fine-Tuning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.14930" class="toolbar-btn" target="_blank">📄 arXiv: 2510.14930v2</a>
  <a href="https://arxiv.org/pdf/2510.14930.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.14930v2" onclick="toggleFavorite(this, '2510.14930v2', 'VT-Refine: Learning Bimanual Assembly with Visuo-Tactile Feedback via Simulation Fine-Tuning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Binghao Huang, Jie Xu, Iretiayo Akinola, Wei Yang, Balakumar Sundaralingam, Rowland O'Flaherty, Dieter Fox, Xiaolong Wang, Arsalan Mousavian, Yu-Wei Chao, Yunzhu Li

**分类**: cs.RO, cs.LG

**发布日期**: 2025-10-16 (更新: 2025-10-18)

**备注**: Accepted by 9th Conference on Robot Learning (CoRL 2025); Website: https://binghao-huang.github.io/vt_refine/

**🔗 代码/项目**: [PROJECT_PAGE](https://binghao-huang.github.io/vt_refine/)

---

## 💡 一句话要点

**VT-Refine：通过模拟微调学习基于视觉-触觉反馈的双臂装配**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `双臂装配` `视觉触觉融合` `强化学习` `模拟微调` `扩散策略` `机器人操作` `触觉传感器`

## 📋 核心要点

1. 人类擅长双臂装配，能适应丰富的触觉反馈，但机器人难以仅通过行为克隆复制，因为人类演示并非最优且多样性有限。
2. VT-Refine框架结合真实演示、高保真触觉模拟和强化学习，首先通过扩散策略学习，再在模拟环境中通过强化学习微调。
3. 实验结果表明，VT-Refine通过增加数据多样性，实现了更有效的策略微调，从而提高了模拟和真实环境中的装配性能。

## 📝 摘要（中文）

本文提出了一种名为VT-Refine的视觉-触觉策略学习框架，用于解决精确且富含接触的双臂装配任务。该框架结合了真实世界的演示、高保真触觉模拟和强化学习。首先，使用同步的视觉和触觉输入，在一个小规模的演示数据集上训练扩散策略。然后，将该策略迁移到配备模拟触觉传感器的模拟数字孪生体中，并通过大规模强化学习进一步优化，以增强鲁棒性和泛化能力。为了实现精确的sim-to-real迁移，利用了高分辨率压阻式触觉传感器，该传感器提供法向力信号，并且可以使用GPU加速模拟进行逼真建模。实验结果表明，VT-Refine通过增加数据多样性并实现更有效的策略微调，提高了模拟和真实世界中的装配性能。

## 🔬 方法详解

**问题定义**：论文旨在解决机器人双臂装配任务中，由于缺乏有效的触觉反馈利用，导致装配精度和鲁棒性不足的问题。现有方法依赖于行为克隆，但人类演示数据质量不高且多样性有限，难以训练出泛化能力强的策略。

**核心思路**：论文的核心思路是结合真实世界的少量演示数据和模拟环境中的大量强化学习数据，利用高保真触觉模拟弥补真实数据不足，并通过强化学习提升策略的鲁棒性和泛化能力。这种方法旨在克服单纯依赖行为克隆的局限性。

**技术框架**：VT-Refine框架包含两个主要阶段：1) 基于真实演示的策略初始化：使用真实世界的视觉和触觉数据训练一个扩散策略，作为后续强化学习的初始策略。2) 基于模拟环境的策略微调：将初始策略迁移到模拟环境中，利用强化学习算法（具体算法未知）进行大规模训练，优化策略以适应不同的装配场景和扰动。

**关键创新**：该方法最重要的创新点在于结合了真实演示和高保真触觉模拟，并利用强化学习进行策略微调。通过这种方式，可以有效地利用少量真实数据和大量模拟数据，提高策略的泛化能力和鲁棒性。此外，使用高分辨率压阻式触觉传感器，并进行精确的模拟，也是实现sim-to-real迁移的关键。

**关键设计**：论文使用了扩散策略进行初始策略的学习，具体扩散模型的结构和训练细节未知。在模拟环境中，使用了GPU加速的触觉模拟，以提高训练效率。强化学习算法的具体选择和奖励函数的设计未知，但奖励函数的设计对于策略的性能至关重要。压阻式触觉传感器的建模精度和参数设置也是影响sim-to-real迁移效果的关键因素。

## 📊 实验亮点

论文通过实验验证了VT-Refine框架的有效性，在模拟和真实环境中都取得了显著的性能提升。具体的性能数据和对比基线未知，但论文强调VT-Refine通过增加数据多样性和实现更有效的策略微调，提高了装配成功率和鲁棒性。高保真触觉模拟和强化学习的结合是取得良好效果的关键。

## 🎯 应用场景

该研究成果可应用于各种需要精确操作和力反馈的机器人装配任务，例如电子产品组装、精密仪器制造、医疗器械装配等。通过提高机器人的装配精度和鲁棒性，可以降低生产成本，提高生产效率，并实现更复杂的自动化装配流程。未来，该技术有望应用于更广泛的机器人操作任务中。

## 📄 摘要（原文）

> Humans excel at bimanual assembly tasks by adapting to rich tactile feedback -- a capability that remains difficult to replicate in robots through behavioral cloning alone, due to the suboptimality and limited diversity of human demonstrations. In this work, we present VT-Refine, a visuo-tactile policy learning framework that combines real-world demonstrations, high-fidelity tactile simulation, and reinforcement learning to tackle precise, contact-rich bimanual assembly. We begin by training a diffusion policy on a small set of demonstrations using synchronized visual and tactile inputs. This policy is then transferred to a simulated digital twin equipped with simulated tactile sensors and further refined via large-scale reinforcement learning to enhance robustness and generalization. To enable accurate sim-to-real transfer, we leverage high-resolution piezoresistive tactile sensors that provide normal force signals and can be realistically modeled in parallel using GPU-accelerated simulation. Experimental results show that VT-Refine improves assembly performance in both simulation and the real world by increasing data diversity and enabling more effective policy fine-tuning. Our project page is available at https://binghao-huang.github.io/vt_refine/.

