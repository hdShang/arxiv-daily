---
layout: default
title: "ProVox: Personalization and Proactive Planning for Situated Human-Robot Collaboration"
---

# ProVox: Personalization and Proactive Planning for Situated Human-Robot Collaboration

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.12248" class="toolbar-btn" target="_blank">📄 arXiv: 2506.12248v1</a>
  <a href="https://arxiv.org/pdf/2506.12248.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.12248v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.12248v1', 'ProVox: Personalization and Proactive Planning for Situated Human-Robot Collaboration')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jennifer Grannen, Siddharth Karamcheti, Blake Wulfe, Dorsa Sadigh

**分类**: cs.RO, cs.AI, cs.CL, cs.HC, cs.LG

**发布日期**: 2025-06-13

**备注**: Accepted by IEEE Robotics and Automation Letters 2025

---

## 💡 一句话要点

**提出ProVox框架以解决人机协作中的主动规划问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `人机协作` `主动规划` `个性化` `元提示` `任务规划` `机器人技术` `家庭服务机器人`

## 📋 核心要点

1. 现有的协作机器人在理解人类意图和偏好方面存在不足，导致用户需要频繁地进行明确指令。
2. ProVox框架通过元提示协议，使用户能够在交互前传达偏好，机器人则利用这些信息主动规划行为。
3. 实验表明，ProVox在家庭任务中提高了协作效率，减少了用户的指导负担，表现出显著的性能提升。

## 📝 摘要（中文）

协作机器人必须快速适应人类伙伴的意图和偏好，以主动识别有帮助的行动。本文提出ProVox（“主动语音”）框架，使机器人能够从早期互动中推断伙伴的目标，并在用户明确指令之前主动规划行为。通过设计元提示协议，用户可以在物理交互开始前传达其独特的偏好和意图。ProVox利用个性化提示来调节任务规划，建议有助的行动，从而减轻用户负担。实验结果表明，ProVox在家庭操作任务中显著提高了协作效率，任务完成时间提高了38.7%，用户负担减少了31.9%。

## 🔬 方法详解

**问题定义**：本文旨在解决协作机器人在理解人类意图和偏好方面的不足，现有方法往往需要用户频繁提供明确指令，增加了用户的负担。

**核心思路**：ProVox框架的核心思想是通过元提示协议，使用户能够在物理交互开始前传达其独特的偏好和意图，从而使机器人能够主动规划行为，减少对用户指令的依赖。

**技术框架**：ProVox的整体架构包括用户输入的元提示模块、个性化的语言模型任务规划器和主动行为建议模块。用户通过元提示传达信息，机器人根据这些信息进行任务规划。

**关键创新**：ProVox的主要创新在于结合了大语言模型的常识先验和可调性，使机器人能够在没有明确指令的情况下，主动推测用户的意图并进行行为规划。这与传统方法的被动响应形成鲜明对比。

**关键设计**：在设计中，元提示协议的参数设置至关重要，确保用户的偏好能够被准确捕捉和理解。此外，任务规划器的损失函数和网络结构经过优化，以提高机器人对用户意图的推断能力。

## 📊 实验亮点

实验结果显示，ProVox在家庭操作任务中的表现显著优于非主动基线，任务完成时间提高了38.7%，用户负担减少了31.9%。这些结果表明，元提示和主动规划在提升人机协作效率方面至关重要。

## 🎯 应用场景

ProVox框架具有广泛的应用潜力，尤其是在家庭服务机器人、医疗辅助机器人和工业协作机器人等领域。通过提高机器人对人类意图的理解和主动响应能力，ProVox能够显著提升人机协作的效率和用户体验，未来可能推动智能机器人在日常生活中的普及和应用。

## 📄 摘要（原文）

> Collaborative robots must quickly adapt to their partner's intent and preferences to proactively identify helpful actions. This is especially true in situated settings where human partners can continually teach robots new high-level behaviors, visual concepts, and physical skills (e.g., through demonstration), growing the robot's capabilities as the human-robot pair work together to accomplish diverse tasks. In this work, we argue that robots should be able to infer their partner's goals from early interactions and use this information to proactively plan behaviors ahead of explicit instructions from the user. Building from the strong commonsense priors and steerability of large language models, we introduce ProVox ("Proactive Voice"), a novel framework that enables robots to efficiently personalize and adapt to individual collaborators. We design a meta-prompting protocol that empowers users to communicate their distinct preferences, intent, and expected robot behaviors ahead of starting a physical interaction. ProVox then uses the personalized prompt to condition a proactive language model task planner that anticipates a user's intent from the current interaction context and robot capabilities to suggest helpful actions; in doing so, we alleviate user burden, minimizing the amount of time partners spend explicitly instructing and supervising the robot. We evaluate ProVox through user studies grounded in household manipulation tasks (e.g., assembling lunch bags) that measure the efficiency of the collaboration, as well as features such as perceived helpfulness, ease of use, and reliability. Our analysis suggests that both meta-prompting and proactivity are critical, resulting in 38.7% faster task completion times and 31.9% less user burden relative to non-active baselines. Supplementary material, code, and videos can be found at https://provox-2025.github.io.

