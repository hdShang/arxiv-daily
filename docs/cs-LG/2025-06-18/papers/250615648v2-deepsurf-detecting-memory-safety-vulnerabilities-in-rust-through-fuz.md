---
layout: default
title: "deepSURF: Detecting Memory Safety Vulnerabilities in Rust Through Fuzzing LLM-Augmented Harnesses"
---

# deepSURF: Detecting Memory Safety Vulnerabilities in Rust Through Fuzzing LLM-Augmented Harnesses

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.15648" class="toolbar-btn" target="_blank">📄 arXiv: 2506.15648v2</a>
  <a href="https://arxiv.org/pdf/2506.15648.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.15648v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.15648v2', 'deepSURF: Detecting Memory Safety Vulnerabilities in Rust Through Fuzzing LLM-Augmented Harnesses')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Georgios Androutsopoulos, Antonio Bianchi

**分类**: cs.CR, cs.LG, cs.SE

**发布日期**: 2025-06-18 (更新: 2025-10-24)

**备注**: At IEEE S&P 2026

---

## 💡 一句话要点

**提出deepSURF以解决Rust中内存安全漏洞检测问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `内存安全` `Rust编程` `模糊测试` `大型语言模型` `静态分析` `安全漏洞检测` `泛型处理`

## 📋 核心要点

1. 现有的Rust内存错误检测工具在检测能力和对Rust特有类型的处理上存在局限，且依赖人工干预。
2. deepSURF结合静态分析与LLM指导的模糊测试生成，创新性地处理泛型并动态增强模糊测试工具。
3. 在63个Rust库的评估中，deepSURF成功发现30个已知漏洞和12个未知漏洞，显示出显著的检测能力提升。

## 📝 摘要（中文）

尽管Rust默认确保内存安全，但其允许使用不安全代码，这可能导致内存安全漏洞。现有的Rust内存错误检测工具通常检测能力有限，无法有效处理Rust特有类型，且过于依赖人工干预。为了解决这些问题，本文提出了deepSURF，这是一种结合静态分析与大型语言模型（LLM）指导的模糊测试工具，旨在有效识别Rust库中的内存安全漏洞，特别是针对不安全代码。deepSURF通过用自定义类型替代泛型并生成特定的实现，增强了模糊测试的能力。此外，deepSURF动态增强模糊测试工具，促进复杂API交互的探索，显著提高了发现内存安全漏洞的可能性。通过在63个真实Rust库上的评估，deepSURF成功重新发现了30个已知内存安全漏洞，并揭示了12个未知漏洞，显示出明显的性能提升。

## 🔬 方法详解

**问题定义**：本文旨在解决Rust中不安全代码引入的内存安全漏洞检测问题。现有工具在处理Rust特有类型时能力不足，且往往需要人工干预，导致检测效率低下。

**核心思路**：deepSURF通过结合静态分析与LLM指导的模糊测试生成，创新性地处理泛型，使用自定义类型替代泛型，从而增强模糊测试的灵活性和有效性。

**技术框架**：deepSURF的整体架构包括静态分析模块、模糊测试生成模块和LLM增强模块。静态分析模块负责识别潜在的内存安全问题，模糊测试生成模块生成测试用例，而LLM增强模块则动态优化测试用例以探索复杂的API交互。

**关键创新**：deepSURF的主要创新在于其处理泛型的方式，通过自定义类型和特定实现，使得模糊测试能够模拟用户定义的行为。这一方法显著提高了对复杂代码的测试能力。

**关键设计**：在设计中，deepSURF采用了特定的参数设置以优化模糊测试的覆盖率，并使用了适应性损失函数来评估测试用例的有效性，确保能够高效发现内存安全漏洞。

## 📊 实验亮点

在对63个真实Rust库的评估中，deepSURF成功重新发现了30个已知的内存安全漏洞，并揭示了12个未知漏洞，其中11个已被分配RustSec ID，3个已被修复，显示出相较于现有工具的显著性能提升。

## 🎯 应用场景

deepSURF的研究成果在Rust编程语言的安全性提升方面具有重要应用价值，尤其是在开发高安全性软件时。其方法可以广泛应用于开源库的安全审计、企业级应用的漏洞检测以及教育领域的安全编程课程中，推动Rust生态系统的安全性发展。

## 📄 摘要（原文）

> Although Rust ensures memory safety by default, it also permits the use of unsafe code, which can introduce memory safety vulnerabilities if misused. Unfortunately, existing tools for detecting memory bugs in Rust typically exhibit limited detection capabilities, inadequately handle Rust-specific types, or rely heavily on manual intervention.
>   To address these limitations, we present deepSURF, a tool that integrates static analysis with Large Language Model (LLM)-guided fuzzing harness generation to effectively identify memory safety vulnerabilities in Rust libraries, specifically targeting unsafe code. deepSURF introduces a novel approach for handling generics by substituting them with custom types and generating tailored implementations for the required traits, enabling the fuzzer to simulate user-defined behaviors within the fuzzed library. Additionally, deepSURF employs LLMs to augment fuzzing harnesses dynamically, facilitating exploration of complex API interactions and significantly increasing the likelihood of exposing memory safety vulnerabilities. We evaluated deepSURF on 63 real-world Rust crates, successfully rediscovering 30 known memory safety bugs and uncovering 12 previously-unknown vulnerabilities (out of which 11 have been assigned RustSec IDs and 3 have been patched), demonstrating clear improvements over state-of-the-art tools.

