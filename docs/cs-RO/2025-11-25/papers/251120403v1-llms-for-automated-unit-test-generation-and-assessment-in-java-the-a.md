---
layout: default
title: LLMs for Automated Unit Test Generation and Assessment in Java: The AgoneTest Framework
---

# LLMs for Automated Unit Test Generation and Assessment in Java: The AgoneTest Framework

**arXiv**: [2511.20403v1](https://arxiv.org/abs/2511.20403) | [PDF](https://arxiv.org/pdf/2511.20403.pdf)

**作者**: Andrea Lops, Fedelucio Narducci, Azzurra Ragone, Michelantonio Trizio, Claudio Barto

---

## 💡 一句话要点

**提出AgoneTest框架以自动化评估Java中LLM生成的单元测试**

**关键词**: `单元测试生成` `大型语言模型评估` `Java测试框架` `变异测试` `测试气味检测`

## 📋 核心要点

1. 单元测试资源密集，需自动化评估LLM生成测试的质量
2. 框架提供标准化评估流程，集成数据集和指标如变异得分
3. 实验显示LLM生成测试在编译子集中可媲美人工测试

## 📄 摘要（原文）

> Unit testing is an essential but resource-intensive step in software development, ensuring individual code units function correctly. This paper introduces AgoneTest, an automated evaluation framework for Large Language Model-generated (LLM) unit tests in Java. AgoneTest does not aim to propose a novel test generation algorithm; rather, it supports researchers and developers in comparing different LLMs and prompting strategies through a standardized end-to-end evaluation pipeline under realistic conditions. We introduce the Classes2Test dataset, which maps Java classes under test to their corresponding test classes, and a framework that integrates advanced evaluation metrics, such as mutation score and test smells, for a comprehensive assessment. Experimental results show that, for the subset of tests that compile, LLM-generated tests can match or exceed human-written tests in terms of coverage and defect detection. Our findings also demonstrate that enhanced prompting strategies contribute to test quality. AgoneTest clarifies the potential of LLMs in software testing and offers insights for future improvements in model design, prompt engineering, and testing practices.

