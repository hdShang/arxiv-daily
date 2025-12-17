---
layout: default
title: Impact of Robot Facial-Audio Expressions on Human Robot Trust Dynamics and Trust Repair
---

# Impact of Robot Facial-Audio Expressions on Human Robot Trust Dynamics and Trust Repair

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.13981" class="toolbar-btn" target="_blank">📄 arXiv: 2512.13981</a>
  <a href="https://arxiv.org/pdf/2512.13981.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.13981" onclick="toggleFavorite(this, '2512.13981', 'Impact of Robot Facial-Audio Expressions on Human Robot Trust Dynamics and Trust Repair')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hossein Naderi, Alireza Shojaei, Philip Agee, Kereshmeh Afsari, Abiola Akanmu

**分类**: cs.RO

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**研究机器人面部-音频表情对人机信任动态及修复的影响，应用于建筑行业人机协作。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `人机交互` `信任动态` `情感表达` `机器人道歉` `建筑机器人`

## 📋 核心要点

1. 现有研究多将人机协作中的信任视为静态因素，缺乏对协作过程中信任动态变化的指导。
2. 通过设计机器人面部-音频表情，在任务成功或失败后做出相应反馈，观察对人类信任的影响。
3. 实验表明，机器人成功提升信任，失败降低信任，道歉表情可部分恢复信任，且年龄会影响信任动态。

## 📝 摘要（中文）

本文研究了在建筑行业人机协作中，机器人的任务表现及其结果后的表达性反应如何影响人类信任的动态变化。设计了一个受建筑启发的受控实验，包含材料递送（物理辅助）和信息收集（感知辅助）两个任务。使用包含14个条目的HRI信任感知量表和重新委派选择，重复测量信任（每个任务四次）。机器人产生两种多模态表达：成功后显示“高兴”表情并简短确认，失败后显示“悲伤”表情并道歉和请求第二次机会。实验在实验室环境中进行，有30名参与者和一个四足机器人平台。评估了两个任务中的信任动态和修复。结果表明，机器人成功可靠地增加了信任，失败导致信任急剧下降，基于道歉的表达部分恢复了信任（材料递送中恢复44％；信息收集中恢复38％）。项目级分析表明，恢复的信任主要受交互和沟通因素驱动，能力部分恢复，而自主性方面变化最小。此外，年龄组和先前的态度调节了信任动态，年轻参与者表现出更大但持续时间更短的变化，20多岁的参与者表现出最持久的修复，而年长的参与者表现出最保守的动态。这项工作为未来的工作奠定了基础，这些工作使修复策略适应任务需求和用户资料，以支持在建筑工地安全，高效地采用机器人。

## 🔬 方法详解

**问题定义**：论文旨在解决人机协作中，尤其是在建筑行业，如何动态地理解和修复人类对机器人的信任问题。现有方法通常将信任视为静态变量，忽略了任务表现和机器人表达对信任的动态影响。这种静态视角无法有效指导机器人如何根据实时情况调整行为，以维持或恢复人类的信任。

**核心思路**：论文的核心思路是研究机器人在任务成功或失败后，通过面部和音频表情表达情绪，观察这些表达对人类信任动态的影响。通过让机器人在成功时表现出“高兴”，失败时表现出“悲伤”并道歉，模拟人类的情感反馈，从而考察这种情感表达是否能够修复因失败而受损的信任。

**技术框架**：该研究采用了一个受控的实验设计，包含两个任务：材料递送（物理辅助）和信息收集（感知辅助）。参与者与一个四足机器人平台进行交互，完成这些任务。在每个任务中，机器人都可能成功或失败。在任务完成后，机器人会根据结果展示相应的面部和音频表情。研究人员使用HRI信任感知量表和重新委派选择，在每个任务中重复测量参与者对机器人的信任程度。

**关键创新**：该研究的关键创新在于关注了机器人情感表达对信任动态的影响，并量化了不同情感表达（如道歉）在信任修复中的作用。此外，研究还考察了年龄等个体差异对信任动态的调节作用，这为设计更具适应性的人机交互系统提供了依据。

**关键设计**：实验中，机器人使用预先设计好的面部和音频表情来表达“高兴”和“悲伤”两种情绪。信任感知量表包含14个条目，用于评估参与者对机器人的信任程度。重新委派选择则用于衡量参与者是否愿意将任务再次委托给机器人。研究还记录了参与者的年龄和先前对机器人的态度，作为调节变量进行分析。

## 📊 实验亮点

实验结果表明，机器人成功可以显著提升人类信任，而失败会导致信任急剧下降。道歉表情能够部分恢复信任，在材料递送任务中恢复了44%，在信息收集任务中恢复了38%。此外，研究发现年轻参与者对机器人的信任变化更为敏感，而年长参与者则表现出更为保守的信任动态。

## 🎯 应用场景

该研究成果可应用于建筑、制造、医疗等领域的人机协作场景。通过赋予机器人适当的情感表达能力，可以有效提升人类对机器人的信任，从而提高协作效率和安全性。未来的研究可以进一步探索更复杂的情感表达方式，并根据不同任务和用户特征定制个性化的信任修复策略。

## 📄 摘要（原文）

> Despite recent advances in robotics and human-robot collaboration in the AEC industry, trust has mostly been treated as a static factor, with little guidance on how it changes across events during collaboration. This paper investigates how a robot's task performance and its expressive responses after outcomes shape the dynamics of human trust over time. To this end, we designed a controlled within-subjects study with two construction-inspired tasks, Material Delivery (physical assistance) and Information Gathering (perceptual assistance), and measured trust repeatedly (four times per task) using the 14-item Trust Perception Scale for HRI plus a redelegation choice. The robot produced two multimodal expressions, a "glad" display with a brief confirmation after success, and a "sad" display with an apology and a request for a second chance after failure. The study was conducted in a lab environment with 30 participants and a quadruped platform, and we evaluated trust dynamics and repair across both tasks. Results show that robot success reliably increases trust, failure causes sharp drops, and apology-based expressions partially restores trust (44% recovery in Material Delivery; 38% in Information Gathering). Item-level analysis indicates that recovered trust was driven mostly by interaction and communication factors, with competence recovering partially and autonomy aspects changing least. Additionally, age group and prior attitudes moderated trust dynamics with younger participants showed larger but shorter-lived changes, mid-20s participants exhibited the most durable repair, and older participants showed most conservative dynamics. This work provides a foundation for future efforts that adapt repair strategies to task demands and user profiles to support safe, productive adoption of robots on construction sites.

