---
layout: default
title: Automating eHMI Action Design with LLMs for Automated Vehicle Communication
---

# Automating eHMI Action Design with LLMs for Automated Vehicle Communication

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20711" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20711v2</a>
  <a href="https://arxiv.org/pdf/2505.20711.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20711v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20711v2', 'Automating eHMI Action Design with LLMs for Automated Vehicle Communication')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ding Xia, Xinyue Gui, Fan Gao, Dongyuan Li, Mark Colley, Takeo Igarashi

**分类**: cs.HC, cs.RO

**发布日期**: 2025-05-27 (更新: 2025-10-10)

**备注**: Accepted as findings for EMNLP 2025

---

## 💡 一句话要点

**利用大语言模型自动设计eHMI动作以提升自动驾驶车辆沟通能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自动驾驶` `人机界面` `大语言模型` `动作设计` `交通沟通` `3D渲染` `自动评分`

## 📋 核心要点

1. 现有的eHMI研究依赖于预定义文本和手动设计的动作，缺乏在动态场景中的适应性。
2. 本文提出一个集成LLMs与3D渲染器的管道，利用LLMs自动生成eHMI动作，提升信息传递的灵活性。
3. 通过收集320个动作序列的数据集，验证了LLMs在动作设计中的有效性，尤其是推理能力强的模型表现更佳。

## 📝 摘要（中文）

自动驾驶车辆（AVs）与其他道路使用者之间缺乏明确的沟通渠道，因此需要外部人机界面（eHMI）有效传达信息。现有的eHMI研究多依赖预定义文本消息和手动设计的动作，这限制了其在动态场景中的适应性。本文提出利用大语言模型（LLMs）作为自动化动作设计工具，验证其在信息传递中的有效性。我们提出了一个集成LLMs和3D渲染器的管道，收集了320个动作序列的数据集，并引入了两种自动评分机制，结果表明LLMs能够接近人类水平地将意图消息转化为动作。

## 🔬 方法详解

**问题定义**：本文旨在解决自动驾驶车辆与其他道路使用者之间缺乏有效沟通的问题。现有方法依赖于静态的文本和手动设计的动作，无法适应复杂和动态的交通场景。

**核心思路**：我们提出利用大语言模型（LLMs）作为自动化动作设计工具，能够根据不同的交通场景和意图消息生成相应的eHMI动作，从而提高沟通的灵活性和有效性。

**技术框架**：整体架构包括三个主要模块：首先，LLMs负责生成可执行的动作；其次，3D渲染器用于渲染这些动作的视觉效果；最后，自动评分机制评估生成动作的质量与人类偏好的匹配度。

**关键创新**：最重要的创新在于将LLMs与3D渲染技术结合，形成一个自动化的动作设计管道，显著提升了eHMI的适应性和实用性。与传统方法相比，该方法能够更灵活地应对不同的交通场景。

**关键设计**：在设计中，我们设置了特定的参数以优化LLMs的输出，并采用了两种自动评分机制（动作参考分数和视觉语言模型）来评估生成动作的质量，确保其与人类偏好的高度一致性。

## 📊 实验亮点

实验结果表明，利用LLMs生成的动作在接近人类水平的评分中表现优异，尤其是推理能力强的模型在不同eHMI模态下的适应性更强。通过引入自动评分机制，我们能够有效评估和优化生成的动作，提升了整体系统的性能。

## 🎯 应用场景

该研究的潜在应用领域包括自动驾驶车辆的安全沟通系统、智能交通管理和人机交互设计等。通过提升eHMI的适应性，能够有效改善自动驾驶车辆在复杂交通环境中的沟通能力，增强道路安全性。未来，该技术有望推广至更广泛的智能交通系统中，促进人机协作的进一步发展。

## 📄 摘要（原文）

> The absence of explicit communication channels between automated vehicles (AVs) and other road users requires the use of external Human-Machine Interfaces (eHMIs) to convey messages effectively in uncertain scenarios. Currently, most eHMI studies employ predefined text messages and manually designed actions to perform these messages, which limits the real-world deployment of eHMIs, where adaptability in dynamic scenarios is essential. Given the generalizability and versatility of large language models (LLMs), they could potentially serve as automated action designers for the message-action design task. To validate this idea, we make three contributions: (1) We propose a pipeline that integrates LLMs and 3D renderers, using LLMs as action designers to generate executable actions for controlling eHMIs and rendering action clips. (2) We collect a user-rated Action-Design Scoring dataset comprising a total of 320 action sequences for eight intended messages and four representative eHMI modalities. The dataset validates that LLMs can translate intended messages into actions close to a human level, particularly for reasoning-enabled LLMs. (3) We introduce two automated raters, Action Reference Score (ARS) and Vision-Language Models (VLMs), to benchmark 18 LLMs, finding that the VLM aligns with human preferences yet varies across eHMI modalities.

