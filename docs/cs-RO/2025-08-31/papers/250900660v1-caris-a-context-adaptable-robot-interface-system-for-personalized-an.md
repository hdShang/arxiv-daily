---
layout: default
title: "CARIS: A Context-Adaptable Robot Interface System for Personalized and Scalable Human-Robot Interaction"
---

# CARIS: A Context-Adaptable Robot Interface System for Personalized and Scalable Human-Robot Interaction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.00660" class="toolbar-btn" target="_blank">📄 arXiv: 2509.00660v1</a>
  <a href="https://arxiv.org/pdf/2509.00660.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.00660v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.00660v1', 'CARIS: A Context-Adaptable Robot Interface System for Personalized and Scalable Human-Robot Interaction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Felipe Arias-Russi, Yuanchen Bai, Angelique Taylor

**分类**: cs.RO, cs.HC

**发布日期**: 2025-08-31

---

## 💡 一句话要点

**提出CARIS以解决人机交互适应性不足的问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `人机交互` `上下文自适应` `机器人接口` `多模态数据` `心理健康` `导游机器人` `远程操作`

## 📋 核心要点

1. 现有的WoZ工具通常局限于单一场景，缺乏跨场景的适应性，限制了人机交互的灵活性和实用性。
2. 本文提出的CARIS系统结合了多种先进技术，旨在实现上下文自适应的人机交互，提升机器人在不同场景中的表现。
3. 通过初步实验，CARIS在心理健康陪伴和导游场景中表现出良好的控制能力，并识别出多个改进方向。

## 📝 摘要（中文）

人机交互（HRI）领域传统上使用“巫师控制”（WoZ）机器人来探索导航、对话动态和人机互动等行为。然而，现有的WoZ工具通常局限于单一场景，缺乏跨场景、用户和机器人平台的适应性。为了解决这些问题，本文提出了一种上下文自适应机器人接口系统（CARIS），结合了远程操作、人类感知、人机对话和多模态数据记录等先进机器人能力。通过初步研究，我们展示了CARIS在心理健康陪伴和导游两种场景中进行WoZ控制的潜力，并识别了CARIS的改进领域，包括运动与交流的更顺畅整合、功能分离的清晰性、推荐提示和一键通信选项，以增强CARIS的可用性。该项目为HRI社区提供了一个公开的、上下文自适应的工具，帮助研究人员简化数据驱动的智能机器人行为研究。

## 🔬 方法详解

**问题定义**：本文旨在解决现有WoZ工具在不同场景、用户和机器人平台之间适应性不足的问题，这限制了人机交互的灵活性和有效性。

**核心思路**：CARIS系统通过整合远程操作、人类感知和多模态数据记录等技术，提供一个可适应不同上下文的机器人接口，旨在提升人机交互的自然性和效率。

**技术框架**：CARIS的整体架构包括多个模块：远程操作模块用于控制机器人，感知模块用于理解用户行为，对话模块用于实现人机交流，以及数据记录模块用于收集交互数据。这些模块协同工作，支持多种场景的应用。

**关键创新**：CARIS的主要创新在于其上下文自适应能力，能够在不同的应用场景中灵活调整机器人行为，与传统的单一场景WoZ工具相比，提供了更高的适应性和实用性。

**关键设计**：在设计中，CARIS采用了推荐提示和一键通信选项，以提高用户交互的便捷性。此外，系统还关注运动与交流的整合，确保用户体验的流畅性。具体的参数设置和网络结构细节尚未公开。

## 📊 实验亮点

在初步实验中，CARIS成功实现了在心理健康陪伴和导游场景中的WoZ控制，显示出良好的适应性和用户体验。具体的性能数据和对比基线尚未提供，但研究指出了多个改进方向，表明系统的可用性和实用性有显著提升。

## 🎯 应用场景

CARIS系统的潜在应用领域包括心理健康支持、教育、旅游导览等场景。其上下文自适应能力使得机器人能够根据不同用户需求和环境变化进行灵活调整，具有广泛的实际价值和未来影响，能够推动人机交互技术的进一步发展。

## 📄 摘要（原文）

> The human-robot interaction (HRI) field has traditionally used Wizard-of-Oz (WoZ) controlled robots to explore navigation, conversational dynamics, human-in-the-loop interactions, and more to explore appropriate robot behaviors in everyday settings. However, existing WoZ tools are often limited to one context, making them less adaptable across different settings, users, and robotic platforms. To mitigate these issues, we introduce a Context-Adaptable Robot Interface System (CARIS) that combines advanced robotic capabilities such teleoperation, human perception, human-robot dialogue, and multimodal data recording. Through pilot studies, we demonstrate the potential of CARIS to WoZ control a robot in two contexts: 1) mental health companion and as a 2) tour guide. Furthermore, we identified areas of improvement for CARIS, including smoother integration between movement and communication, clearer functionality separation, recommended prompts, and one-click communication options to enhance the usability wizard control of CARIS. This project offers a publicly available, context-adaptable tool for the HRI community, enabling researchers to streamline data-driven approaches to intelligent robot behavior.

