use pyo3::prelude::*;
use pyo3::wrap_pyfunction;

use monte_carlo_pi::monte_carlo_pi;

#[pyfunction]
fn mcpi(iterations: u32) -> PyResult<(f64, String)> {
    Ok(monte_carlo_pi(iterations as u32))
}

#[pymodule]
fn montecarlo3pi(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(mcpi, m)?)?;

    Ok(())
}
