---
layout: default
title: OmniVIC: A Self-Improving Variable Impedance Controller with Vision-Language In-Context Learning for Safe Robotic Manipulation
---

# OmniVIC: A Self-Improving Variable Impedance Controller with Vision-Language In-Context Learning for Safe Robotic Manipulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.17150" class="toolbar-btn" target="_blank">📄 arXiv: 2510.17150v2</a>
  <a href="https://arxiv.org/pdf/2510.17150.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.17150v2" onclick="toggleFavorite(this, '2510.17150v2', 'OmniVIC: A Self-Improving Variable Impedance Controller with Vision-Language In-Context Learning for Safe Robotic Manipulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Heng Zhang, Wei-Hsing Huang, Gokhan Solak, Arash Ajoudani

**分类**: cs.RO

**发布日期**: 2025-10-20 (更新: 2025-10-22)

**备注**: Code, video and RAG dataset are available at \url{https://sites.google.com/view/omni-vic}

---

## 💡 一句话要点

**OmniVIC：基于视觉语言上下文学习的自提升变阻抗控制器，用于安全机器人操作**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `变阻抗控制` `视觉语言模型` `上下文学习` `机器人操作` `人机协作`

## 📋 核心要点

1. 传统变阻抗控制器在复杂、非结构化环境中泛化性不足，难以应对接触型任务中的不确定性。
2. OmniVIC利用视觉语言模型和上下文学习，根据图像和自然语言描述自适应调整阻抗参数，实现安全交互。
3. 实验表明，OmniVIC在模拟和真实机器人任务中，成功率显著提升，力违规情况减少。

## 📝 摘要（中文）

本文提出了一种通用的变阻抗控制器(VIC)——OmniVIC，它通过视觉语言模型(VLM)增强，提高了任何接触型机器人操作任务中的安全性和适应性，从而增强了安全物理交互。传统的VIC在机器人与环境进行物理交互时表现出优势，但在涉及接触或不确定性的通用任务场景中，对于未见过的、复杂的和非结构化的安全交互缺乏泛化能力。为此，所提出的OmniVIC解释了从图像和自然语言中推导出的任务上下文，并为VIC控制器生成自适应阻抗参数。具体来说，OmniVIC的核心是自提升的检索增强生成(RAG)和上下文学习(ICL)，其中RAG从结构化记忆库中检索相关的先前经验，以告知控制器关于类似的过去任务，ICL利用这些检索到的例子和当前任务的提示来查询VLM，从而为当前的操纵场景生成上下文感知和自适应的阻抗参数。因此，自提升的RAG和ICL保证了OmniVIC在通用任务场景中的工作。阻抗参数的调节进一步由实时力/力矩反馈告知，以确保交互力保持在安全阈值内。我们证明了我们的方法在模拟和真实机器人任务的一系列复杂接触型任务中优于基线，具有更高的成功率和更少的力违规。OmniVIC朝着桥接高层语义推理和低层顺应控制迈出了一步，从而实现了更安全和更通用的操作。总体而言，平均成功率从27%（基线）提高到61.4%（OmniVIC）。

## 🔬 方法详解

**问题定义**：现有机器人变阻抗控制方法在处理复杂、未知的接触型任务时，泛化能力不足。它们难以根据任务的上下文信息（如视觉输入和自然语言描述）动态调整阻抗参数，导致安全性降低和任务失败率升高。现有方法难以有效利用历史经验，缺乏自适应能力。

**核心思路**：OmniVIC的核心思路是利用视觉语言模型（VLM）理解任务的上下文信息，并结合检索增强生成（RAG）和上下文学习（ICL）机制，从历史经验中学习，从而为变阻抗控制器生成自适应的阻抗参数。通过实时力/力矩反馈，进一步保证交互力在安全阈值内。

**技术框架**：OmniVIC的整体框架包括以下几个主要模块：1) 视觉语言模型（VLM）：用于理解图像和自然语言描述，提取任务的上下文信息。2) 检索增强生成（RAG）：从结构化记忆库中检索与当前任务相关的历史经验。3) 上下文学习（ICL）：利用检索到的历史经验和当前任务的上下文信息，通过VLM生成自适应的阻抗参数。4) 变阻抗控制器（VIC）：根据生成的阻抗参数控制机器人的运动。5) 力/力矩传感器：实时监测交互力，并反馈给控制器，以保证安全性。

**关键创新**：OmniVIC的关键创新在于：1) 将视觉语言模型引入变阻抗控制，实现了高层语义推理和低层顺应控制的桥接。2) 提出了自提升的RAG和ICL机制，使控制器能够从历史经验中学习，提高泛化能力。3) 结合实时力/力矩反馈，进一步增强了安全性。与现有方法相比，OmniVIC能够更好地理解任务的上下文信息，并生成更合适的阻抗参数。

**关键设计**：RAG模块使用结构化记忆库存储历史任务的图像、自然语言描述和阻抗参数。ICL模块使用Prompt工程，将检索到的历史经验和当前任务的上下文信息作为Prompt输入VLM，生成阻抗参数。阻抗参数包括刚度、阻尼等。力/力矩反馈用于调整阻抗参数，防止交互力超过安全阈值。具体VLM模型选择、Prompt设计、记忆库构建方式等细节未在摘要中明确说明。

## 📊 实验亮点

实验结果表明，OmniVIC在模拟和真实机器人任务中均优于基线方法。平均成功率从基线的27%提高到61.4%，力违规情况显著减少。这表明OmniVIC能够有效地理解任务的上下文信息，并生成合适的阻抗参数，从而提高任务的成功率和安全性。

## 🎯 应用场景

OmniVIC具有广泛的应用前景，可用于各种需要安全物理交互的机器人操作任务，如装配、抓取、操作工具等。该研究有助于提升机器人在复杂、非结构化环境中的适应性和安全性，促进人机协作机器人的发展，并可应用于医疗、制造、服务等领域。

## 📄 摘要（原文）

> We present OmniVIC, a universal variable impedance controller (VIC) enhanced by a vision language model (VLM), which improves safety and adaptation in any contact-rich robotic manipulation task to enhance safe physical interaction. Traditional VIC have shown advantages when the robot physically interacts with the environment, but lack generalization in unseen, complex, and unstructured safe interactions in universal task scenarios involving contact or uncertainty. To this end, the proposed OmniVIC interprets task context derived reasoning from images and natural language and generates adaptive impedance parameters for a VIC controller. Specifically, the core of OmniVIC is a self-improving Retrieval-Augmented Generation(RAG) and in-context learning (ICL), where RAG retrieves relevant prior experiences from a structured memory bank to inform the controller about similar past tasks, and ICL leverages these retrieved examples and the prompt of current task to query the VLM for generating context-aware and adaptive impedance parameters for the current manipulation scenario. Therefore, a self-improved RAG and ICL guarantee OmniVIC works in universal task scenarios. The impedance parameter regulation is further informed by real-time force/torque feedback to ensure interaction forces remain within safe thresholds. We demonstrate that our method outperforms baselines on a suite of complex contact-rich tasks, both in simulation and on real-world robotic tasks, with improved success rates and reduced force violations. OmniVIC takes a step towards bridging high-level semantic reasoning and low-level compliant control, enabling safer and more generalizable manipulation. Overall, the average success rate increases from 27% (baseline) to 61.4% (OmniVIC).

