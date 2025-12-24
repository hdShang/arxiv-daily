---
layout: default
title: "AnyTask: an Automated Task and Data Generation Framework for Advancing Sim-to-Real Policy Learning"
---

# AnyTask: an Automated Task and Data Generation Framework for Advancing Sim-to-Real Policy Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.17853" class="toolbar-btn" target="_blank">📄 arXiv: 2512.17853v1</a>
  <a href="https://arxiv.org/pdf/2512.17853.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.17853v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.17853v1', 'AnyTask: an Automated Task and Data Generation Framework for Advancing Sim-to-Real Policy Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ran Gong, Xiaohan Zhang, Jinghuan Shang, Maria Vittoria Minniti, Jigarkumar Patel, Valerio Pepe, Riedana Yan, Ahmet Gundogdu, Ivan Kapelyukh, Ali Abbas, Xiaoqiang Yan, Harsh Patel, Laura Herlant, Karl Schmeckpeper

**分类**: cs.RO, cs.AI

**发布日期**: 2025-12-19

**备注**: 28 pages, 25 figures. The first four authors contributed equally

---

## 💡 一句话要点

**AnyTask：自动化任务与数据生成框架，推进Sim-to-Real策略学习**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `机器人学习` `Sim-to-Real` `自动化任务生成` `专家演示` `行为克隆`

## 📋 核心要点

1. 真实世界机器人数据收集成本高昂，仿真成为重要替代方案，但任务设计、场景生成和迁移仍需大量人工。
2. AnyTask框架结合GPU并行仿真与基础模型，自动化设计多样操作任务并合成机器人数据，降低人工成本。
3. 通过ViPR等Agent生成专家演示，训练的行为克隆策略在真实机器人上实现了44%的平均成功率。

## 📝 摘要（中文）

通用机器人学习受到数据限制：大规模、多样化和高质量的交互数据在现实世界中收集成本高昂。虽然仿真已成为扩展数据收集的一种有希望的方式，但相关任务，包括仿真任务设计、任务感知场景生成、专家演示合成和Sim-to-Real迁移，仍然需要大量的人工干预。我们提出了AnyTask，一个自动化框架，它将大规模并行GPU仿真与基础模型相结合，以设计多样化的操作任务并合成机器人数据。我们引入了三个AnyTask Agent，用于生成旨在解决尽可能多任务的专家演示：1) ViPR，一种新颖的任务和运动规划Agent，具有VLM-in-the-loop并行优化；2) ViPR-Eureka，一种强化学习Agent，具有生成的密集奖励和LLM引导的接触采样；3) ViPR-RL，一种混合规划和学习方法，它仅使用稀疏奖励共同产生高质量的演示。我们在生成的数据上训练行为克隆策略，在仿真中验证它们，并将它们直接部署在真实机器人硬件上。这些策略推广到新的物体姿势，在真实世界的抓取放置、抽屉打开、富接触推和长时程操作任务套件中实现了44%的平均成功率。

## 🔬 方法详解

**问题定义**：现有机器人学习方法依赖于大量真实世界数据，但数据收集成本高昂且耗时。仿真环境可以生成大量数据，但任务设计、场景生成、专家演示合成以及从仿真到真实的迁移仍然需要大量的人工干预。这限制了通用机器人学习的发展。

**核心思路**：AnyTask的核心思路是利用大规模并行GPU仿真和基础模型，自动化地生成多样化的操作任务和高质量的机器人数据。通过自动化任务设计和数据生成流程，降低对人工干预的依赖，从而加速Sim-to-Real策略学习。

**技术框架**：AnyTask框架包含以下几个主要模块：1) 任务设计模块：利用基础模型自动生成多样化的操作任务。2) 场景生成模块：根据任务需求自动生成任务相关的场景。3) 专家演示合成模块：使用ViPR、ViPR-Eureka和ViPR-RL等Agent生成高质量的专家演示数据。4) 策略训练模块：使用生成的数据训练行为克隆策略。5) Sim-to-Real迁移模块：将训练好的策略部署到真实机器人上。

**关键创新**：AnyTask的关键创新在于自动化任务和数据生成流程，特别是ViPR Agent的设计。ViPR Agent采用VLM-in-the-loop并行优化，能够有效地生成高质量的专家演示数据。此外，ViPR-Eureka Agent利用LLM引导的接触采样，提高了强化学习的效率。ViPR-RL Agent则结合了规划和学习方法，在稀疏奖励下也能生成高质量的演示。

**关键设计**：ViPR Agent的关键设计包括：1) VLM-in-the-loop：利用视觉语言模型（VLM）来评估任务完成情况，并指导任务规划。2) 并行优化：利用GPU并行计算能力，同时优化多个任务规划方案，提高效率。3) 奖励函数设计：ViPR-Eureka Agent设计了基于LLM的密集奖励函数，引导Agent学习。4) 接触采样：ViPR-Eureka Agent利用LLM引导的接触采样，提高探索效率。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17853v1/figures_and_tables/draft_main_figure.jpg" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17853v1/figures_and_tables/vipr_improvement.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17853v1/x1.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，使用AnyTask框架生成的数据训练的行为克隆策略，在真实世界的抓取放置、抽屉打开、富接触推和长时程操作任务套件中实现了44%的平均成功率。该策略能够推广到新的物体姿势，证明了AnyTask框架的有效性和泛化能力。相较于其他方法，AnyTask显著降低了人工干预的需求，提高了数据生成的效率。

## 🎯 应用场景

AnyTask框架可应用于各种机器人操作任务，例如工业自动化、家庭服务机器人、医疗机器人等。通过自动化任务设计和数据生成，可以降低机器人学习的成本，加速机器人在复杂环境中的部署。该框架还有助于推动通用机器人学习的发展，使机器人能够适应各种不同的任务和环境。

## 📄 摘要（原文）

> Generalist robot learning remains constrained by data: large-scale, diverse, and high-quality interaction data are expensive to collect in the real world. While simulation has become a promising way for scaling up data collection, the related tasks, including simulation task design, task-aware scene generation, expert demonstration synthesis, and sim-to-real transfer, still demand substantial human effort. We present AnyTask, an automated framework that pairs massively parallel GPU simulation with foundation models to design diverse manipulation tasks and synthesize robot data. We introduce three AnyTask agents for generating expert demonstrations aiming to solve as many tasks as possible: 1) ViPR, a novel task and motion planning agent with VLM-in-the-loop Parallel Refinement; 2) ViPR-Eureka, a reinforcement learning agent with generated dense rewards and LLM-guided contact sampling; 3) ViPR-RL, a hybrid planning and learning approach that jointly produces high-quality demonstrations with only sparse rewards. We train behavior cloning policies on generated data, validate them in simulation, and deploy them directly on real robot hardware. The policies generalize to novel object poses, achieving 44% average success across a suite of real-world pick-and-place, drawer opening, contact-rich pushing, and long-horizon manipulation tasks. Our project website is at https://anytask.rai-inst.com .

