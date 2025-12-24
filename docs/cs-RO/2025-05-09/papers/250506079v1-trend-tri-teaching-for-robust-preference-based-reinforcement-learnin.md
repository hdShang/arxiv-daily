---
layout: default
title: "TREND: Tri-teaching for Robust Preference-based Reinforcement Learning with Demonstrations"
---

# TREND: Tri-teaching for Robust Preference-based Reinforcement Learning with Demonstrations

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.06079" class="toolbar-btn" target="_blank">📄 arXiv: 2505.06079v1</a>
  <a href="https://arxiv.org/pdf/2505.06079.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.06079v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.06079v1', 'TREND: Tri-teaching for Robust Preference-based Reinforcement Learning with Demonstrations')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shuaiyi Huang, Mara Levy, Anubhav Gupta, Daniel Ekpo, Ruijie Zheng, Abhinav Shrivastava

**分类**: cs.RO, cs.CV

**发布日期**: 2025-05-09

**备注**: ICRA 2025

**🔗 代码/项目**: [PROJECT_PAGE](https://shuaiyihuang.github.io/publications/)

---

## 💡 一句话要点

**提出TREND框架以解决偏好反馈噪声问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `偏好强化学习` `噪声处理` `机器人操作` `三重教学` `专家演示` `鲁棒性` `知识传递`

## 📋 核心要点

1. 现有的偏好强化学习方法在处理人类反馈时，常常受到噪声的影响，导致学习效果不佳。
2. TREND框架通过三重教学策略，结合少量专家演示，提升了对噪声偏好反馈的鲁棒性。
3. 在多种机器人操作任务中，TREND在高达40%的噪声水平下仍能实现90%的成功率，显示出显著的性能提升。

## 📝 摘要（中文）

偏好反馈通常由人类或视觉语言模型（VLM）注释者收集，但这些反馈往往存在噪声，这对依赖准确偏好标签的偏好强化学习构成了重大挑战。为了解决这一问题，本文提出了TREND框架，该框架结合了少量专家演示和三重教学策略，以有效减轻噪声影响。我们的方案同时训练三个奖励模型，每个模型将其小损失偏好对视为有用知识，并将这些有用对传授给其同伴网络以更新参数。值得注意的是，我们的方法只需一到三个专家演示即可实现高性能。我们在多种机器人操作任务上评估了TREND，即使在高达40%的噪声水平下，成功率也达到了90%，突显了其在处理噪声偏好反馈方面的有效鲁棒性。

## 🔬 方法详解

**问题定义**：本文旨在解决偏好反馈中存在的噪声问题，现有方法在面对噪声时表现不佳，影响学习效果。

**核心思路**：TREND框架通过三重教学策略，利用少量专家演示来训练三个奖励模型，使其相互学习，从而有效减轻噪声的影响。

**技术框架**：TREND的整体架构包括三个主要模块：三个奖励模型的并行训练、模型间的知识传递以及对小损失偏好对的利用。每个模型独立学习，同时又通过共享有用知识来增强整体性能。

**关键创新**：TREND的核心创新在于三重教学策略的引入，使得模型能够在噪声环境中相互促进，显著提高了学习的鲁棒性。这一方法与传统的单一模型训练方式有本质区别。

**关键设计**：在模型训练中，采用了特定的损失函数来强调小损失偏好对的价值，并设计了适应性参数设置，以确保模型在不同噪声水平下的稳定性和有效性。具体的网络结构和参数设置在实验中经过优化，以达到最佳性能。

## 📊 实验亮点

在多种机器人操作任务中，TREND框架在高达40%的噪声水平下实现了90%的成功率，显示出其在噪声环境中的强大鲁棒性。与传统方法相比，TREND在处理偏好反馈时的表现显著提升，展示了其有效性和实用性。

## 🎯 应用场景

TREND框架在机器人操作、自动驾驶、智能家居等领域具有广泛的应用潜力。通过提高偏好强化学习的鲁棒性，该方法能够在实际环境中更好地处理人类反馈，提升智能系统的决策能力和适应性，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Preference feedback collected by human or VLM annotators is often noisy, presenting a significant challenge for preference-based reinforcement learning that relies on accurate preference labels. To address this challenge, we propose TREND, a novel framework that integrates few-shot expert demonstrations with a tri-teaching strategy for effective noise mitigation. Our method trains three reward models simultaneously, where each model views its small-loss preference pairs as useful knowledge and teaches such useful pairs to its peer network for updating the parameters. Remarkably, our approach requires as few as one to three expert demonstrations to achieve high performance. We evaluate TREND on various robotic manipulation tasks, achieving up to 90% success rates even with noise levels as high as 40%, highlighting its effective robustness in handling noisy preference feedback. Project page: https://shuaiyihuang.github.io/publications/TREND.

