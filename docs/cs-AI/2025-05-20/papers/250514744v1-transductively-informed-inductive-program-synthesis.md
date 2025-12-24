---
layout: default
title: Transductively Informed Inductive Program Synthesis
---

# Transductively Informed Inductive Program Synthesis

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14744" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14744v1</a>
  <a href="https://arxiv.org/pdf/2505.14744.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14744v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14744v1', 'Transductively Informed Inductive Program Synthesis')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Janis Zenkner, Tobias Sesterhenn, Christian Bartelt

**分类**: cs.PL, cs.AI, cs.LG

**发布日期**: 2025-05-20

---

## 💡 一句话要点

**提出TIIPS框架以提升程序合成的准确性与泛化能力**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `程序合成` `归纳学习` `传导学习` `机器学习` `自动化编程` `智能编程` `模型融合`

## 📋 核心要点

1. 现有程序合成方法在归纳与传导模型的结合上存在不足，未能有效建模两者的交互。
2. 本文提出TIIPS框架，通过合作机制将归纳与传导策略统一，提升程序合成的准确性与泛化能力。
3. 实验结果表明，TIIPS在字符串和列表操作领域解决了更多任务，且生成的函数在语法和语义上更接近最优解。

## 📝 摘要（中文）

程序合成中的抽象与推理在归纳与传导范式下取得了显著进展。归纳方法通过输入输出示例生成程序，而传导方法则直接为给定输入预测输出值。现有方法通过孤立的集成结合这两种模型，但未明确建模两者之间的交互。本文提出了TIIPS框架，通过合作机制显式建模归纳与传导策略的交互：归纳模型生成程序，传导模型约束、指导并优化搜索，从而提高合成的准确性与泛化能力。我们在字符串和列表操作的程序合成领域对TIIPS进行了评估，结果显示其在任务解决和语法语义上更接近最优解，尤其在分布外设置中表现出色，达到了最先进的性能。

## 🔬 方法详解

**问题定义**：本文旨在解决程序合成中归纳与传导模型之间的交互建模不足的问题。现有方法往往孤立地结合这两种模型，导致合成准确性和泛化能力的不足。

**核心思路**：TIIPS框架通过合作机制将归纳模型与传导模型结合，归纳模型负责生成程序，而传导模型则约束和优化搜索过程，从而提升合成效果。

**技术框架**：TIIPS框架包括两个主要模块：归纳模型和传导模型。归纳模型生成潜在程序，传导模型则根据输入输出示例对生成的程序进行约束和指导，形成一个闭环反馈机制。

**关键创新**：TIIPS的创新在于显式建模归纳与传导推理之间的协同作用，这一设计使得两者能够互相促进，显著提高了合成的准确性和泛化能力。

**关键设计**：在模型设计上，TIIPS采用了特定的损失函数来平衡归纳与传导模型的输出，同时在网络结构上进行了优化，以确保模型能够有效地捕捉输入输出之间的复杂关系。具体参数设置和网络结构细节在实验部分进行了详细说明。

## 📊 实验亮点

实验结果显示，TIIPS在字符串和列表操作的程序合成任务中解决了更多问题，生成的函数在语法和语义上更接近最优解。在分布外设置中，TIIPS的性能达到了最先进水平，展示了其在实际应用中的强大能力。

## 🎯 应用场景

TIIPS框架在程序合成领域具有广泛的应用潜力，能够用于自动化代码生成、软件开发辅助工具以及教育领域的编程教学。其显著提升的合成准确性和泛化能力，预示着在更复杂的编程任务中也能发挥重要作用，推动智能编程技术的发展。

## 📄 摘要（原文）

> Abstraction and reasoning in program synthesis has seen significant progress through both inductive and transductive paradigms. Inductive approaches generate a program or latent function from input-output examples, which can then be applied to new inputs. Transductive approaches directly predict output values for given inputs, effectively serving as the function themselves. Current approaches combine inductive and transductive models via isolated ensembling, but they do not explicitly model the interaction between both paradigms. In this work, we introduce \acs{tiips}, a novel framework that unifies transductive and inductive strategies by explicitly modeling their interactions through a cooperative mechanism: an inductive model generates programs, while a transductive model constrains, guides, and refines the search to improve synthesis accuracy and generalization. We evaluate \acs{tiips} on two widely studied program synthesis domains: string and list manipulation. Our results show that \acs{tiips} solves more tasks and yields functions that more closely match optimal solutions in syntax and semantics, particularly in out-of-distribution settings, yielding state-of-the-art performance. We believe that explicitly modeling the synergy between inductive and transductive reasoning opens promising avenues for general-purpose program synthesis and broader applications.

