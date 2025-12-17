---
layout: default
title: A Reason-then-Describe Instruction Interpreter for Controllable Video Generation
---

# A Reason-then-Describe Instruction Interpreter for Controllable Video Generation

**arXiv**: [2511.20563v1](https://arxiv.org/abs/2511.20563) | [PDF](https://arxiv.org/pdf/2511.20563.pdf)

**作者**: Shengqiong Wu, Weicai Ye, Yuanxing Zhang, Jiahao Wang, Quande Liu, Xintao Wang, Pengfei Wan, Kun Gai, Hao Fei, Tat-Seng Chua

---

## 💡 一句话要点

**提出ReaDe指令解释器以解决可控视频生成中的意图输出不匹配问题**

**关键词**: `可控视频生成` `指令解释器` `扩散变换器` `两阶段优化` `意图对齐`

## 📋 核心要点

1. 核心问题：用户指令简洁模糊，与训练详细提示不匹配，导致可控性受限
2. 方法要点：采用原因-描述范式，先解析用户需求，再生成详细指导
3. 实验效果：在单/多条件场景中提升指令忠实度、字幕准确性和视频质量

## 📄 摘要（原文）

> Diffusion Transformers have significantly improved video fidelity and temporal coherence, however, practical controllability remains limited. Concise, ambiguous, and compositionally complex user inputs contrast with the detailed prompts used in training, yielding an intent-output mismatch. We propose ReaDe, a universal, model-agnostic interpreter that converts raw instructions into precise, actionable specifications for downstream video generators. ReaDe follows a reason-then-describe paradigm: it first analyzes the user request to identify core requirements and resolve ambiguities, then produces detailed guidance that enables faithful, controllable generation. We train ReaDe via a two-stage optimization: (i) reasoning-augmented supervision imparts analytic parsing with stepwise traces and dense captions, and (ii) a multi-dimensional reward assigner enables stable, feedback-driven refinement for natural-style captions. Experiments across single- and multi-condition scenarios show consistent gains in instruction fidelity, caption accuracy, and downstream video quality, with strong generalization to reasoning-intensive and unseen inputs. ReaDe offers a practical route to aligning controllable video generation with accurately interpreted user intent. Project Page: https://sqwu.top/ReaDe/.

