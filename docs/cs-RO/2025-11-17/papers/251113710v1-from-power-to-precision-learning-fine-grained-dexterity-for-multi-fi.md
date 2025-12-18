---
layout: default
title: From Power to Precision: Learning Fine-grained Dexterity for Multi-fingered Robotic Hands
---

# From Power to Precision: Learning Fine-grained Dexterity for Multi-fingered Robotic Hands

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.13710" class="toolbar-btn" target="_blank">📄 arXiv: 2511.13710v1</a>
  <a href="https://arxiv.org/pdf/2511.13710.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.13710v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.13710v1', 'From Power to Precision: Learning Fine-grained Dexterity for Multi-fingered Robotic Hands')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jianglong Ye, Lai Wei, Guangqi Jiang, Changwei Jing, Xueyan Zou, Xiaolong Wang

**分类**: cs.RO, cs.AI, cs.LG

**发布日期**: 2025-11-17

**备注**: Project page: https://jianglongye.com/power-to-precision

---

## 💡 一句话要点

**联合优化控制与指尖几何，提升多指灵巧手精细操作能力**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `多指灵巧手` `精细操作` `协同设计` `sim-to-real` `神经物理仿真`

## 📋 核心要点

1. 现有机器人手在力量抓取上表现良好，但在精细操作方面仍有不足，难以兼顾力量与精细。
2. 通过联合优化控制策略和指尖几何形状，实现力量抓取和精细操作之间的动态切换。
3. 实验表明，该方法在sim-to-real和real-to-real环境中均表现出色，显著提升了精细操作能力。

## 📝 摘要（中文）

人类抓取可大致分为力量抓取和精细抓取。精细抓取促进了工具的使用，并被认为影响了人类的进化。目前的多指机器人手在力量抓取方面表现出色，但对于需要精细操作的任务，平行夹爪仍然更受欢迎。这突显了当前机器人手设计的一个关键局限：难以在单个通用系统中同时实现稳定的力量抓取和精确的精细操作。本文通过联合优化多指灵巧手的控制和硬件设计来弥合这一差距，从而实现力量和精细操作。我们没有重新设计整个手，而是引入了一种轻量级的指尖几何形状修改，将其表示为接触平面，并与其对应的控制参数一起进行优化。我们的控制策略动态地在力量和精细操作之间切换，并将精细控制简化为拇指-食指的平行运动，这证明了其在sim-to-real迁移中的鲁棒性。在设计方面，我们利用大规模仿真，使用可微分的神经物理代理模型来优化指尖几何形状。我们通过在sim-to-real和real-to-real设置中的大量实验验证了我们的方法。我们的方法在sim-to-real精细抓取中，对未见物体的零样本成功率达到了82.5%，在涉及面包捏取的具有挑战性的真实世界任务中，成功率达到了93.3%。这些结果表明，我们的协同设计框架可以显著提高多指手的精细操作能力，而不会降低其力量抓取能力。项目主页位于https://jianglongye.com/power-to-precision。

## 🔬 方法详解

**问题定义**：现有机器人手难以同时实现稳定可靠的力量抓取和精确的精细操作，导致在需要精细操作的场景中，平行夹爪仍然更受欢迎。多指灵巧手的设计和控制复杂，难以实现两种抓取方式的有效切换和优化。

**核心思路**：通过协同优化控制策略和指尖几何形状，使得多指手能够动态地在力量抓取和精细操作之间切换。核心在于简化精细操作的控制，并利用可微分的神经物理模型优化指尖设计。

**技术框架**：该方法包含两个主要部分：控制策略优化和指尖几何形状优化。控制策略采用动态切换机制，在力量抓取和精细操作之间切换，并将精细操作简化为拇指-食指的平行运动。指尖几何形状优化则利用大规模仿真，通过可微分的神经物理代理模型来优化指尖的接触平面参数。整体流程是先进行控制策略的训练，然后利用训练好的控制策略作为优化目标，优化指尖几何形状。

**关键创新**：该方法的核心创新在于协同优化控制策略和硬件设计（指尖几何形状），而不是单独优化控制或重新设计整个手。通过将指尖几何形状表示为接触平面，并利用可微分的神经物理模型进行优化，实现了高效的硬件设计优化。此外，将精细操作简化为拇指-食指的平行运动，降低了控制的复杂性，提高了鲁棒性。

**关键设计**：指尖几何形状被参数化为一个接触平面，其参数包括位置和方向。控制策略采用动态切换机制，根据任务需求在力量抓取和精细操作之间切换。损失函数包括抓取稳定性和操作精度两部分，用于指导指尖几何形状的优化。神经物理代理模型用于加速仿真过程，提高优化效率。

## 📊 实验亮点

该方法在sim-to-real精细抓取中，对未见物体的零样本成功率达到了82.5%，显著优于传统方法。在具有挑战性的真实世界任务（面包捏取）中，成功率达到了93.3%，证明了该方法在实际应用中的有效性。这些结果表明，通过协同优化控制和硬件设计，可以显著提升多指手的精细操作能力。

## 🎯 应用场景

该研究成果可应用于需要精细操作的机器人应用场景，例如医疗手术机器人、精密装配机器人、以及家庭服务机器人等。通过提升机器人手的灵巧性和适应性，可以使其更好地完成各种复杂任务，提高工作效率和服务质量，具有广阔的应用前景。

## 📄 摘要（原文）

> Human grasps can be roughly categorized into two types: power grasps and precision grasps. Precision grasping enables tool use and is believed to have influenced human evolution. Today's multi-fingered robotic hands are effective in power grasps, but for tasks requiring precision, parallel grippers are still more widely adopted. This contrast highlights a key limitation in current robotic hand design: the difficulty of achieving both stable power grasps and precise, fine-grained manipulation within a single, versatile system. In this work, we bridge this gap by jointly optimizing the control and hardware design of a multi-fingered dexterous hand, enabling both power and precision manipulation. Rather than redesigning the entire hand, we introduce a lightweight fingertip geometry modification, represent it as a contact plane, and jointly optimize its parameters along with the corresponding control. Our control strategy dynamically switches between power and precision manipulation and simplifies precision control into parallel thumb-index motions, which proves robust for sim-to-real transfer. On the design side, we leverage large-scale simulation to optimize the fingertip geometry using a differentiable neural-physics surrogate model. We validate our approach through extensive experiments in both sim-to-real and real-to-real settings. Our method achieves an 82.5% zero-shot success rate on unseen objects in sim-to-real precision grasping, and a 93.3% success rate in challenging real-world tasks involving bread pinching. These results demonstrate that our co-design framework can significantly enhance the fine-grained manipulation ability of multi-fingered hands without reducing their ability for power grasps. Our project page is at https://jianglongye.com/power-to-precision

