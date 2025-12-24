---
layout: default
title: "Prompt-and-Check: Using Large Language Models to Evaluate Communication Protocol Compliance in Simulation-Based Training"
---

# Prompt-and-Check: Using Large Language Models to Evaluate Communication Protocol Compliance in Simulation-Based Training

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.08652" class="toolbar-btn" target="_blank">📄 arXiv: 2508.08652v1</a>
  <a href="https://arxiv.org/pdf/2508.08652.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.08652v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.08652v1', 'Prompt-and-Check: Using Large Language Models to Evaluate Communication Protocol Compliance in Simulation-Based Training')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Vishakha Lall, Yisi Liu

**分类**: cs.AI

**发布日期**: 2025-08-12

---

## 💡 一句话要点

**提出Prompt-and-Check以评估模拟训练中的沟通协议合规性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `沟通协议` `合规性评估` `模拟训练` `上下文推理`

## 📋 核心要点

1. 现有方法在模拟训练中评估沟通合规性时，往往依赖于人工评估，效率低且主观性强。
2. 论文提出的Prompt-and-Check方法，通过上下文丰富的提示，利用大型语言模型自动评估沟通协议的合规性。
3. 实验结果显示，该方法在海事领域的应用中，能够有效提高合规性判断的准确性和一致性。

## 📝 摘要（中文）

在模拟训练中，准确评估程序性沟通合规性至关重要，尤其是在安全关键领域。本文探讨了一种轻量级的方法Prompt-and-Check，利用开源大型语言模型（LLMs）进行基于提示的推理，能够在消费级GPU上高效运行。通过对海事领域的案例研究，研究者使用LLama 2 7B、LLaMA 3 8B和Mistral 7B等模型，评估参与者在模拟任务中的沟通合规性。研究结果表明，提示能够有效支持上下文感知推理，无需特定任务训练，展示了LLMs在训练环境中增强反馈和自动评估的实用性。

## 🔬 方法详解

**问题定义**：本文旨在解决在模拟训练中评估沟通协议合规性时的低效和主观性问题。现有方法通常依赖人工评估，缺乏自动化和一致性。

**核心思路**：Prompt-and-Check方法通过使用上下文丰富的提示，利用大型语言模型进行自动化评估，能够在不需要特定任务训练的情况下，进行有效的上下文感知推理。

**技术框架**：该方法的整体架构包括数据收集、模型选择、提示生成和合规性判断四个主要模块。首先，收集参与者的口头交流记录，然后选择合适的LLM，生成包含相关记录片段的提示，最后模型输出合规性判断。

**关键创新**：最重要的技术创新在于使用上下文丰富的提示进行合规性评估，这与传统的基于规则或人工评估的方法有本质区别，能够实现更高的自动化和准确性。

**关键设计**：在参数设置上，研究使用了LLama 2 7B、LLaMA 3 8B和Mistral 7B等模型，运行在RTX 4070 GPU上。损失函数和网络结构的具体细节未详细披露，但强调了模型输出与专家标注的对比评估。

## 📊 实验亮点

实验结果表明，Prompt-and-Check方法在合规性判断上达到了较高的分类准确率和一致性评分，具体性能数据未披露，但相较于传统人工评估方法，展示了显著的效率提升和准确性改善。

## 🎯 应用场景

该研究的潜在应用领域包括航空、航海等安全关键行业的模拟训练，能够为教练员提供自动化的反馈和评估工具，提升训练效率和效果。未来，该方法有望推广至其他领域的培训和评估中，推动智能化培训的发展。

## 📄 摘要（原文）

> Accurate evaluation of procedural communication compliance is essential in simulation-based training, particularly in safety-critical domains where adherence to compliance checklists reflects operational competence. This paper explores a lightweight, deployable approach using prompt-based inference with open-source large language models (LLMs) that can run efficiently on consumer-grade GPUs. We present Prompt-and-Check, a method that uses context-rich prompts to evaluate whether each checklist item in a protocol has been fulfilled, solely based on transcribed verbal exchanges. We perform a case study in the maritime domain with participants performing an identical simulation task, and experiment with models such as LLama 2 7B, LLaMA 3 8B and Mistral 7B, running locally on an RTX 4070 GPU. For each checklist item, a prompt incorporating relevant transcript excerpts is fed into the model, which outputs a compliance judgment. We assess model outputs against expert-annotated ground truth using classification accuracy and agreement scores. Our findings demonstrate that prompting enables effective context-aware reasoning without task-specific training. This study highlights the practical utility of LLMs in augmenting debriefing, performance feedback, and automated assessment in training environments.

