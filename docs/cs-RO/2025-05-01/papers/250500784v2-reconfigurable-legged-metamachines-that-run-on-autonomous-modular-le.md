---
layout: default
title: Reconfigurable legged metamachines that run on autonomous modular legs
---

# Reconfigurable legged metamachines that run on autonomous modular legs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.00784" class="toolbar-btn" target="_blank">📄 arXiv: 2505.00784v2</a>
  <a href="https://arxiv.org/pdf/2505.00784.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.00784v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.00784v2', 'Reconfigurable legged metamachines that run on autonomous modular legs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chen Yu, David Matthews, Jingxian Wang, Jing Gu, Douglas Blackiston, Michael Rubenstein, Sam Kriegman

**分类**: cs.RO

**发布日期**: 2025-05-01 (更新: 2025-07-16)

---

## 💡 一句话要点

**提出自主模块化腿部以解决腿部机器形态多样性不足问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `模块化机器人` `腿部机器` `自适应系统` `动态行为学习` `形态多样性`

## 📋 核心要点

1. 现有腿部机器在形态多样性上远不及生物腿部动物，难以适应新任务或应对损伤。
2. 提出自主模块化腿部，具备单自由度关节，能够学习复杂动态行为并自由组合形成变形机器。
3. 实验表明，模块化腿部能够在高度动态环境中快速移动，并具备自我修复能力，展现出多样化的腿部形态。

## 📝 摘要（中文）

腿部机器在灵活性和适应性方面日益增强，但与生物腿部动物相比，其形态多样性仍显不足。现有的腿部机器主要集中在四足和双足架构，难以重新配置以适应新任务或应对损伤。本文提出了一种自主模块化腿部，具有单自由度的关节链接，能够学习复杂的动态行为，并可自由组合形成米级的腿部变形机器。这种设计使得高度动态的模块化代理能够快速移动并在非静态环境中灵活应对，同时具备自我修复和重新设计的能力。每个模块都是一个完整的代理，能够承受深度结构损伤，展现出广泛的新型腿部形态。

## 🔬 方法详解

**问题定义**：本文旨在解决现有腿部机器在形态多样性和适应性不足的问题。传统的四足和双足架构难以应对新任务或损伤，限制了其应用范围。

**核心思路**：提出自主模块化腿部，设计为单自由度的关节链接，能够通过学习实现复杂动态行为，并可自由组合以形成不同形态的腿部变形机器。这样的设计使得机器能够快速适应环境变化。

**技术框架**：整体架构包括模块化腿部的设计、学习算法和组合策略。每个模块作为独立代理，能够进行自我学习和适应，形成一个灵活的腿部变形机器。

**关键创新**：最重要的创新在于模块化设计和自我学习能力，使得腿部机器能够在遭受损伤后仍能维持功能，并快速适应新的任务需求。与传统方法相比，这种设计显著提高了机器的灵活性和适应性。

**关键设计**：关键参数包括模块的关节自由度、学习算法的选择以及组合策略的优化。损失函数设计用于优化模块间的协作和整体运动性能，确保机器在动态环境中的稳定性和灵活性。

## 📊 实验亮点

实验结果显示，模块化腿部在动态环境中表现出色，能够以高速度和灵活性移动。与传统腿部机器人相比，模块化设计使得其在遭受深度结构损伤后仍能保持功能，展现出显著的适应能力和灵活性。

## 🎯 应用场景

该研究的潜在应用领域包括救援机器人、探索机器人以及任何需要在复杂环境中灵活移动的自动化系统。自主模块化腿部的设计使得机器人能够在遭遇损伤时迅速恢复功能，具有重要的实际价值和广泛的应用前景。

## 📄 摘要（原文）

> Legged machines are becoming increasingly agile and adaptive but they have so far lacked the morphological diversity of legged animals, which have been rearranged and reshaped to fill millions of niches. Unlike their biological counterparts, legged machines have largely converged over the past decade to canonical quadrupedal and bipedal architectures that cannot be easily reconfigured to meet new tasks or recover from injury. Here we introduce autonomous modular legs: agile yet minimal, single-degree-of-freedom jointed links that can learn complex dynamic behaviors and may be freely attached to form legged metamachines at the meter scale. This enables rapid repair, redesign, and recombination of highly-dynamic modular agents that move quickly and acrobatically (non-quasistatically) through unstructured environments. Because each module is itself a complete agent, legged metamachines are able to sustain deep structural damage that would completely disable other legged robots. We also show how to encode the vast space of possible body configurations into a compact latent design genome that can be efficiently explored, revealing a wide diversity of novel legged forms.

